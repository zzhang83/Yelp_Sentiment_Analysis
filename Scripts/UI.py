import csv
import sqlite3
import numpy as np
import pandas as pd
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import matplotlib as mpl
import pickle

from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

from wordcloud import WordCloud, STOPWORDS
from collections import Counter

from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
stemmer = SnowballStemmer('english')
wordnet_lemmatizer = WordNetLemmatizer()

#############################In/out############################
def open_file(csvfile):
    reader = pd.read_csv(csvfile)
    return reader

def output_file(df,string):
    df.to_csv(string, index = False)

#############################Word Cloud & Feature Extraction############################

def text_process(data):
    '''
    Takes in a df in format of [text,stars] performs the following:
    1. Lower capital letters
    2. Remove all punctuation
    3. Remove all stopwords
    4. Reduce words to their word stem
    5. Return a list of words

    '''
    for i in range(len(data)):
        line = data[i]
        line = line.lower()  # lower case
        translation = str.maketrans("", "", string.punctuation);
        line = line.translate(translation)
        split = word_tokenize(line)
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        filtered = []
        for token in split:
            if re.search('[a-zA-Z]', token):
                filtered.append(token)
        word = [i for i in filtered if i not in stopwords.words('english')]

        d = [stemmer.stem(word) for word in word]
        d = [wordnet_lemmatizer.lemmatize(word) for word in d]
        data[i] = d
    return data


def top_words(business_id,review_ml ):
    train = review_ml[review_ml['business_id'] == business_id][review_ml['True(1)/Deceptive(0)'] == 'True']
    text = list(train['Review'])  # text
    text = text_process(text)
    text = sum(text, [])

    counts = Counter(text)
    wordcloud = WordCloud(
        background_color='white',
        max_words=100,
        max_font_size=50,
        min_font_size=10,
        random_state=40,

    ).fit_words(counts)
    fig = plt.figure(1)
    plt.imshow(wordcloud)
    plt.axis('off')  # remove axis
    plt.show()


def change_label(x):
    for i in range(len(x)):
        if x[i] >= 3.0:  # good review: stars >=3.0
            x[i] = 1
        else:  # bad review: stars 3.0
            x[i] = 0
    return x


def bigram(business_id, review_ml):
    # only use true review

    train0 = review_ml[review_ml['business_id'] == business_id]
    train = train0[train0['True(1)/Deceptive(0)'] == 'True']
    #print(train.head())
    #train_data = list(train['Review'])  # text
    label = list(train['Stars'])  # ratings
    #print(label)
    train_label = change_label(label)
    #print(train_label)

    # TfidfVectorizer Transform
    transformer = TfidfVectorizer(stop_words='english',
                                  ngram_range=(2, 2))  # "ignore terms that appear in less than 1% of the documents".
    #print(transformer)

    cvectorizer = transformer.fit(train['Review'])
    #print(cvectorizer)
    transformed = cvectorizer.transform(train['Review'])
    #print(transformed)

    # SVM regression
    clf = LinearSVC()
    clf.fit(transformed, train_label)
    coefficients = clf.coef_.ravel()
    #print(coefficients)
    pos_coefficients = np.argsort(coefficients)[-10:]
    neg_coefficients = np.argsort(coefficients)[:10]
    combine = np.hstack([neg_coefficients, pos_coefficients])
    #print("combine:, ",combine)
    #print("coefficients[combine]: ", coefficients[combine])

    plt.figure(figsize=(7, 4))
    #print("fisnish 1")

    colors = ['red' if i < 0 else 'blue' for i in coefficients[combine]]
    #print("finish 2")

    plt.bar(np.arange(len(coefficients[combine])), coefficients[combine], color=colors)
    #print("finish 3")

    feature_names = np.array(cvectorizer.get_feature_names())
    #print("finish 4")
    plt.title('why the restaurant is rated as bad or good ', fontsize=15)
    #print("finish 5")

    plt.xticks(np.arange(0, 2 * 10), feature_names[combine], rotation=40, ha='right')
    #print("finish 6")

    plt.show()
    #print("finish 7")


#############################helper function#############################
def load_database_data(c, zipcode, business_name_input):
    c.execute('''
            SELECT b_id,r.review, r.r_stars
            FROM business, review_fact_table r 
            WHERE postal_code = ? AND name = ? AND r.business_id = b_id''', (zipcode, business_name_input,))
    dataframe = pd.DataFrame(data=c.fetchall(), columns=['business_id', 'review', 'rating'])
    return dataframe
def select_data(c, zipcode, business_name):
    c.execute('''
                SELECT DISTINCT(b_id)
                FROM business, review_fact_table r 
                WHERE postal_code = ? AND name = ? AND r.business_id = b_id''', (zipcode, business_name,))
    single_df = pd.DataFrame(data=c.fetchall(), columns=['business_id'])
    return single_df['business_id'][0]

def fake_ratio(predict, single):
    # Load fake results
    predicted_fake = predict
    # reviews that has only that business id
    reviews = predicted_fake[predicted_fake['business_id'] == single]
    n = reviews.shape[0]
    # print(n)
    fake = reviews.groupby('True(1)/Deceptive(0)').count()['Review'][0]
    # print(fake)
    fake_percentage = fake / n
    # print(fake_percentage)
    return fake_percentage

##############################main######################################
def main():
    #open states and income raw data
    zipcode = input("zipcode:")
    business_name = input("restaurant name:")
    print(zipcode,business_name)

    conn = sqlite3.connect('yelp.db')
    c = conn.cursor()
    predicted_fake = open_file('data/predicted_review.csv')
    # find the business id
    single = select_data(c, zipcode, business_name)
    # print(single)
    fake_review_ratio = fake_ratio(predicted_fake,single)
    print(fake_review_ratio)
    #top_words(single, predicted_fake)
    bigram(single, predicted_fake)

#if __name__=="__main__":
    #main()
main()