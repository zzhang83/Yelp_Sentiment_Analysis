# Machine Learning and Visualization with Yelp Dataset 

Yelp is currently the most widely used restaurant and merchant information software across United States. However, Yelp only provides us a holistic view about restaurant, such as giving overall review score or ratings and only a few reviews out of thousands of reviews.  

The objective of this project is to help yelp users, whether they are business owners or consumers, to find information that better meet their preferences. Specifically, our group mainly focused on improving customers’ understanding of restaurants, new business owners'market knowledge, and existing merchants’ awareness about restaurants’ features.   

* We first obtained and extracted data from Yelp open source, United States Census Bureau, and a research group from Stony Brook University. The data consists Yelp businesses, users, reviews, U.S.income, and fake review labeled data. 

* After cleaned the data, we created a SQL database to store Yelp review data. Our database consists of Yelp businesses, users, reviews_fact_table, and income tables that describe different aspects of the data, which allow us to do effective joining and querying.

* In the first part of this project, we examined the fake review detection data, which consists of 350,000 user reviews. The true and fake reviews in the dataset help us trained a model that predicts the validity of a given review (fake/true).

* In the second part of this work, we examined Yelp’s merchant review data with machine learning techniques as well as natural language processing tools to provide consumers and existing merchants insights from the data. Fitting statistical models to the data, we are able to access the most relevant keywords in the reviews that affect review scores.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

 * *In order to obtain the raw data:*
    1. You would need to download Yelp Open Dataset from https://www.yelp.com/dataset. We mainly focus on business.json, review.json, and        users.json in our project. 
    2. You would need to download Fake review labeled data by following the link in **Machine Learning Training Set.txt** file.
    3. You would be able to directly download **income.csv** and **zip_code_states.csv** from the **data** folder.
 
 
 * *In order to obtain the cleaned data:*
    1. You would be able to obtain a cleaned and merged income and zipcode csv by running **Clean_income_zipcode_data.py** in the **script** folder,or you can just download the **income_zipcode.csv** from **data** folder
    2. You would be able to obtain a cleaned business.csv by just downloading the **business_data.csv** in **data** folder.
    3. You would be able to obtain a cleaned review.csv and users.csv by running **Load&Clean Yelp Dataset.ipynb** in the **script** folder. 
 
 
 * *In order to build the SQL database and have a preliminary view about the data:*
    1. You would need to run **SQL Database & Preliminary Data Visualization.ipynb** in the **script** folder. You would also need to obtain cleaned reviews, income_zipcode, users, and business data and put them in a data folder from the previous section. These data will be used to populate our SQL database. 
 
 
 * *In order to visualize some of the data:*
    1. You would need to run **Visualization_for_Review_Business.ipynb** in the **script** folder.
 
 
 * *In order to run fake review detection machine learning model and using filtered true reviews to extract keywords:*
    1. You would first need to have fake review labeled data obtained from previous section. Then you would need to run **Machine Learning.ipynb** in the **script** folder to predict whether our current reviews are deceptive or trustworthy.
    2. After running **Machine Learning.ipynb**, you would need to run **word_cloud & feature extraction.ipynb** to find the key insights about each restaurant.
 
 
 * *Instead of manually running each machine learning files, we created an API & UI that facilitates the process:*
    NOTE: Because of the large size of our data, we still break down the process into several steps that requiring you to manually run each in order on a single computer. If we have resources to run large datasets in a short amount of time, we would automate the whole process.  
    1. You are able to download **predicted_review.csv** by following instructions in **Predicted Review Results.pdf** in the **data** folder. This csv contains the results of predicted reviews' validiy after you ran "machine learning.ipynb". We saved and uploaded the results for the fake review detection machine learning model to improve your and users' experience by shorten the waiting time since we only ran our models on our own computers. 
    2. After obtained "predicted_review.csv" and the SQL database at your local system by following previous steps, you can run **UI.py** or **User_Interface.ipynb** to initiate the automated program.
    3. You may type in any restaurants and its zipcode in six states (PA, NV, NC, IL, OH, AZ) by following the prompt. The program would present a fake review ratio, which is the percentage of the fake reviews out of the total reviews and a graph demonstrating the top 10 keywords that most positively or negatively influencing the reviews of a restaurant.


## User_Interface:
Taking in an user’s inputs, we first query our database to give us the unique business id that is associated with restaurant’s name and zip code. Loading the csv file with the predicted “deceptive vs. true” labels on the reviews, we only extracted those reviews that are related to the unique business id. 

#### Steps:
1. Open **User_Interface.ipynb** in Scripts folder

<img width="637" alt="screen shot 2017-12-30 at 3 05 37 pm" src="https://user-images.githubusercontent.com/31679696/34452110-f71df3b2-ed72-11e7-8efd-ee7c8db31ea1.png">

2. Type in the name and the zipcode of a restaurant that you would like to search
- Here we typed in 85374 as the zip code and  “pei wei” as the restaurant’s name:

<img width="658" alt="screen shot 2017-12-30 at 3 06 48 pm" src="https://user-images.githubusercontent.com/31679696/34452119-24a808ae-ed73-11e7-9541-b6cb85a9c36e.png">


3. Waiting for the program to run for a couple of minutes, you will get the output:

<img width="699" alt="screen shot 2017-12-30 at 3 07 23 pm" src="https://user-images.githubusercontent.com/31679696/34452121-396970e8-ed73-11e7-88fe-7f8c816b4595.png">


## Blog of our project can be found at:
https://medium.com/@zhiwei_zhang

## Built With

* [Anaconda Distribution](https://www.anaconda.com/download/#macos) - The coding environment
* [Jupyter Notebook](http://jupyter.org/install.html) 

## Authors

* **Kunlun Liu** - [kunlun liu](https://github.com/PurpleBooth)
* **Zhiwei Zhang** - [zhiwei zhang](https://github.com/PurpleBooth)
* **Tong Zhang** - [tong zhang](https://github.com/PurpleBooth)

## Acknowledgments

* Many thanks to our professors Dan Potter, Ugur Cetintemel, and Tim Kraska at Brown University for recommendations.
* Many thanks to Professor Rayana at Stony Brook University for providing the fake review labeled data.
* Many thanks to TAs and online experts who commit useful open resources.

