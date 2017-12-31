## Machine Learning and Visualization with Yelp Dataset 

Yelp is currently the most widely used restaurant and merchant information software across United States. However, Yelp only provides us a holistic view about restaurant, such as giving overall review score or ratings and only a few reviews out of thousands of reviews.  

The objective of this project is to help yelp users, whether they are business owners or consumers, to find information that better meet their preferences. Specifically, our group mainly focused on improving customers’ understanding of restaurants, new business owners'market knowledge, and existing merchants’ awareness about restaurants’ features.   

* We first obtained and extract data from Yelp open source, United States Census Bureau, and a research group from Stony Brook University. The data consisted Yelp businesses, users, reviews, U.S.income, and fake review labeled data. 

* After cleaned the data, we created a SQL database to store Yelp review data. Our database are consists of Yelp businesses, users, reviews_fact_table, and income tables that describe different aspects of the data which allow us to do effective joining and querying.

* In the first part of this project, we examined the fake review detection data, which consists of 350,000 user reviews. The true and fake reviews in the dataset help us trained a model that predicts the validity of a given review (fake/true).

* In the second part of this work, we examined Yelp’s merchant review data with machine learning techniques as well as natural language processing tools to provide consumers and existing merchants insights from the data. Fitting statistical models to the data, we are able to access the most relevant keywords in the reviews that affect review scores.


This repository is organized as below:

### Data:

1. You will need to download Yelp Open Dataset from https://www.yelp.com/dataset. We mainly focus on business.json, review.json, and user.json in our project.
2. You would be able to download Machine Learning Training Set.txt and income and zip_code_states.csv from data file.


### Script:
1. You would be able to obtain a cleaned and merged income and zipcode csv by running **Clean_income_zipcode_data.py**
2. you would be able to load and clean yelp open dataset review.json and business.json by runing **Load and Clean.ipynb**
3. You would be able to get the results for fake review dection by running **Machine Learning.ipynb**
4. You would be able to get the wordcloud and important features by running **word_cloud & feature extraction.ipynb**


### Database & Exploratory Statistics
With cleaned reviews, users, business, income & zip code, and fake review labeled data in five separated csv files, it is essential to connect them in order to reduce the time required for merging and extracting data for later models. We built a SQL database with four out of  five csv files (reviews, business, income & zip code, and users) 

Before jumping right into our machine learning models, we also explored and familiarize ourselves with these datasets through graphs and some preliminary analysis. For each of the above dataset, we tried to find patterns and potential problems which could be useful information or traps in the later machine learning processes. 

By running **SQL Database & Preliminary Data Visualization.ipynb** you would be able to get the result for database and visualization.


### User_Interface:
Taking in an user’s inputs, we first query our database to give us the unique business id that is associated with restaurant’s name and zip code. Loading the csv file with the predicted “deceptive vs. true” labels on the reviews, we only extract those reviews that are related to the unique business id. 

###### Steps:
1. Open **User_Interface.ipynb** in Scripts folder

<img width="637" alt="screen shot 2017-12-30 at 3 05 37 pm" src="https://user-images.githubusercontent.com/31679696/34452110-f71df3b2-ed72-11e7-8efd-ee7c8db31ea1.png">

2. Type in the name and the zipcode of a restaurant that you would like to search
- Here we typed in 85374 as the zip code and  “pei wei” as the restaurant’s name:

<img width="658" alt="screen shot 2017-12-30 at 3 06 48 pm" src="https://user-images.githubusercontent.com/31679696/34452119-24a808ae-ed73-11e7-9541-b6cb85a9c36e.png">


3. Waiting for the program to run for a couple of minutes, you will get the output:

<img width="699" alt="screen shot 2017-12-30 at 3 07 23 pm" src="https://user-images.githubusercontent.com/31679696/34452121-396970e8-ed73-11e7-88fe-7f8c816b4595.png">


### Blog of our project can be found at:
https://medium.com/@zhiwei_zhang

### Built With

* [Anaconda Distribution](https://www.anaconda.com/download/#macos) - The coding environment
* [Jupyter Notebook](http://jupyter.org/install.html) 

### Authors

* **Kunlun Liu** - [kunlun liu](https://github.com/PurpleBooth)
* **Zhiwei Zhang** - [zhiwei zhang](https://github.com/PurpleBooth)
* **Tong Zhang** - [tong zhang](https://github.com/PurpleBooth)

### Acknowledgments

* Many thanks to our professors Dan Potter, Ugur Cetintemel, and Tim Kraska at Brown University
* Many thanks to Professor Rayana at Stony Brook University for providing the fake review labeled data
* Many thanks to TAs and online experts who commit useful open resources

