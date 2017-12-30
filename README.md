### Machine Learning and Visualization with Yelp Dataset 


Yelp is currently the most widely used restaurant and merchant information software across United States. However, Yelp only provides us a holistic view about restaurant, such as giving overall review score or ratings and only a few reviews out of thousands of reviews.  

The objective of this project is to improve Yelp users’ experience. We dived deep into Yelp’s open datasets as well as other data centers to retrieve useful information. Utilizing our complementary plug-in prototype, yelp users, whether they are business owners or consumers, are able to find information that better meet their preferences. Specifically, our group mainly focused on  improving the customers’ understanding of merchants, market knowledge for new business owners, and  existing merchants’ awareness about restaurants’ features.  


This repository is organized as below:

#### Data:

1. You will need to download Yelp Open Dataset from https://www.yelp.com/dataset. We mainly focus on business.json, review.json in our project.
2. You would be able to download income and zip_code_states.csv from data file.


#### Script:
1. You would be able to obtain a clearned and merged income and zipcode csv by running Clean_income_zipcode_data.py
2. you would be able to load and clean yelp open dataset review.json and business.json by runing 'Load and Clean.ipynb'
3. 

#### UI:
Taking in an user’s inputs, we first query our database to give us the unique business id that is associated with restaurant’s name and zip code. Loading the csv file with the predicted “deceptive vs. true” labels on the reviews, we only extract those reviews that are related to the unique business id. 

###### Steps:
1. Open UI jupyter notebook

2. Type in the name and the zipcode of a restaurant that you would like to search
- Here we typed in 85374 as the zip code and  “pei wei” as the restaurant’s name:

3. Waiting for the program to run for a couple of minutes, you will get the output:




#### Blog of our project can be found at:
https://medium.com/@zhiwei_zhang



