#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid green 2px; padding: 20px">
#     
# <b>Hello, Nicholas!</b> We're glad to see you in code-reviewer territory. You've done a great job on the project, but let's get to know each other and make it even better! We have our own atmosphere here and a few rules:
# 
# 
# 1. My name is Alexander. I work as a code reviewer, and my main goal is not to point out your mistakes, but to share my experience and help you become a data analyst.
# 2. We speak on a first-come-first-served basis.
# 3. if you want to write or ask a question, don't be shy. Just choose your color for your comment.  
# 4. this is a training project, you don't have to be afraid of making a mistake.  
# 5. You have an unlimited number of attempts to pass the project.  
# 6. Let's Go!
# 
# 
# ---
# I'll be color-coding comments, please don't delete them:
# 
# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Needs fixing. The block requires some corrections. Work can't be accepted with the red comments.
# </div>
#     
# ---
# 
# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# 
# Remarks. Some recommendations.
# </div>
# 
# ---
# 
# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Success. Everything is done succesfully.
# </div>
#     
# ---
#     
# I suggest that we work on the project in dialogue: if you change something in the project or respond to my comments, write about it. It will be easier for me to track changes if you highlight your comments:   
#     
# <div class="alert alert-info"> <b>Student сomments:</b> Student answer..</div>
#     
# All this will help to make the recheck of your project faster. If you have any questions about my comments, let me know, we'll figure it out together :)   
#     
# ---

# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# An excellent practice is to describe the goal and main steps in your own words (a skill that will help a lot on a final project). It would be good to add the progress and purpose of the study.

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
# 
# You're missing the introductory part of the project. In which you have to describe in the markdown cell the purpose of the study and the course of action. So that the customer immediately understands what the project is about

# 

# For this project, you’ll work with data from Instacart. 
# 
# Instacart is a grocery delivery platform where customers can place a grocery order and have it delivered to them, similar to how Uber Eats and Door Dash work. This particular dataset was publicly released by Instacart in 2017 for a Kaggle competition. Although the original dataset is no longer available on the Instacart website, we’ve created CSV files that contain a modified version of that data. Download these files and use them for your project.
# 
# The dataset we've provided for you has been modified from the original. We've reduced the size of the dataset so that your calculations run faster and we’ve introduced missing and duplicate values. We were also careful to preserve the distributions of the original data when we made our changes.
# 
# Your mission is to clean up the data and prepare a report that gives insight into the shopping habits of Instacart customers. After answering each question, write a brief explanation of your results in a markdown cell of your Jupyter notebook.
# 
# This project will require you to make plots that communicate your results. Make sure that any plots you create have a title, labeled axes, and a legend if necessary; and include plt.show() at the end of each cell with a plot.
# 
# 
# Step 1: Open the data files (/datasets/instacart_orders.csv, /datasets/products.csv, /datasets/aisles.csv, /datasets/departments.csv, and /datasets/order_products.csv) and have a look at the general contents of each table. Note that the files have nonstandard formatting, so you'll need to set certain arguments in pd.read_csv() to read the data correctly. Take a look at the CSV files to get a sense of what those arguments should be.
# 
# Note that order_products.csv contains many rows of data. When a DataFrame has too many rows, info() will not print the non-null counts by default. If you want to to print the non-null counts, include show_counts=True when you call info().
# 
# Step 2: Preprocess the data by doing the following:
# 
# Verify and fix data types (e.g. make sure ID columns are integers)
# Identify and fill in missing values
# Identify and remove duplicate values
# Be sure to explain what types of missing and duplicate values you found, how you filled or removed them, why you used those methods, and why you think these missing and duplicate values may have been present in the dataset.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №3__
# 
# Now correct

# # Step 1A: Import the packages you will need to complete this project

# In[1]:


#initialize the program for data analysis and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# # Step 1B: Create a database schema to track progress like new dataframes and data type conversions and to facilitate QC

# In[2]:


#Create database schema and track colnames (https://app.diagrams.net/#G1e8ZbDHcJM3w_EP9-3ReLBbS-f_4UShl-#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D)

#'/datasets/instacart_orders.csv' colnames= order_id; user_id; order_number; order_dow; order_hour_of_day; days_since_prior_order
#datasets/products.csv', delimiter = ';' colnames = product_id; product_name; aisle_id; department_id
#'/datasets/aisles.csv' colnames = aisle_id; aisle
#'/datasets/departments.csv' colnames = department_id; department
#'/datasets/order_products.csv' colnames = order_id; product_id; add_to_cart_order; reordered


# # Step 1C: Import the datasets 

# In[3]:


#Load datasets as a batch and delimit based on semi-colon

orders = pd.read_csv('/datasets/instacart_orders.csv', delimiter = ';')
products = pd.read_csv('/datasets/products.csv', delimiter = ';')
aisles = pd.read_csv('/datasets/aisles.csv', delimiter = ';')
departments = pd.read_csv('/datasets/departments.csv', delimiter = ';')
order_products = pd.read_csv('/datasets/order_products.csv', delimiter = ';')


# # Step 1D: Check the contents of the data frames individually in the same order presented in the project description

# In[4]:


#Check infos
display(orders.head(5))

orders.info(show_counts=True)


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# 
# It is better to use display() rather than print() to output a dataframe object. This way it will be clearer

# In[5]:


display(products.head(5))

products.info(show_counts=True)


# In[6]:


display(aisles.head(5))

aisles.info(show_counts=True)


# In[7]:


display(departments.head(5))

departments.info(show_counts=True)


# In[8]:


display(order_products.head(5))
order_products.info(show_counts=True)


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# It would be good to comment on the data somehow

# 
# Initial impression from the data is that it is fairly complete and will require some joins to carry through integer values to product names. Through joining, the data is comprehensive enough to perform exploratory data analysis.

# # Step 2A: Preprocess the data by verifying and fixing data types (e.g., making sure that ID columns are integers)
# 
# Step 2: Preprocess the data by doing the following:
# 
# Verify and fix data types (e.g. make sure ID columns are integers)
# Identify and fill in missing values
# Identify and remove duplicate values
# Be sure to explain what types of missing and duplicate values you found, how you filled or removed them, why you used those methods, and why you think these missing and duplicate values may have been present in the dataset.

# ## 'orders' data frame

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# The project description provides a structure to help you build a coherent study. Please organize the results of your work according to these steps. Until this is done, I will not be able to check your work.

# In[9]:


# Verify and fix data types

orders['order_id'] = orders['order_id'].astype(int)
orders['user_id'] = orders['user_id'].astype(int)
orders['order_number'] = orders['order_number'].astype(int)
orders['order_dow'] = orders['order_dow'].astype(int)
orders['order_hour_of_day'] = orders['order_hour_of_day'].astype(int)


# 

# ## `products` data frame

# In[10]:


# Verify and fix data types

products['aisle_id'] = products['aisle_id'].astype(int)
products['product_id'] = products['product_id'].astype(int)
products['department_id'] = products['department_id'].astype(int)


# ## `departments` data frame

# In[11]:


# Verify and fix data types

departments['department_id'] = departments['department_id'].astype(int)


# ## `aisles` data frame

# In[12]:


# Verify and fix data types

aisles['aisle_id'] = aisles['aisle_id'].astype(int)


# 

# ## `order_products` data frame

# In[13]:


# Verify and fix data types

order_products['order_id'] = order_products['order_id'].astype(int)
order_products['product_id'] = order_products['product_id'].astype(int)
order_products['reordered'] = order_products['reordered'].astype(int)


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №2__
# 
# All right

# 

# # Step 2B: Find and remove missing values

# ## `orders` data frame

# In[14]:


# Identify and fill in missing values

orders.fillna(orders.mean(), inplace=True)


# In[15]:


# Identify and remove duplicate values

orders.drop_duplicates(inplace=True)


# ## `products` data frame

# In[16]:


# Identify and fill in missing values

products.fillna(products.mean(), inplace=True)


# In[17]:


# Identify and remove duplicate values

products.drop_duplicates(inplace=True)


# ## `departments` data frame

# In[18]:


# Identify and fill in missing values

departments.fillna(departments.mean(), inplace=True)


# In[19]:


# Identify and remove duplicate values

aisles.drop_duplicates(inplace=True)


# ## `aisles` data frame

# In[20]:


# Identify and fill in missing values

aisles.fillna(aisles.mean(), inplace=True)


# In[21]:


# Identify and remove duplicate values

departments.drop_duplicates(inplace=True)


# ## `order_products` data frame

# In[22]:


# Identify and fill in missing values

order_products.fillna(order_products.mean(), inplace=True)


# In[23]:


# Identify and remove duplicate values

order_products.drop_duplicates(inplace=True)


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №2__
# 
# Duplicate checking is the basis of data preprocessing

# 

# # Step 3A: Once all data is preprocessed and ready for analysis, perform the following analysis: 
# 
# [A] (must complete all to pass)
# 
# Verify that values in the 'order_hour_of_day' and 'order_dow' columns in the orders table are sensible (i.e. 'order_hour_of_day' ranges from 0 to 23 and 'order_dow' ranges from 0 to 6).
# Create a plot that shows how many people place orders for each hour of the day.
# Create a plot that shows what day of the week people shop for groceries.
# Create a plot that shows how long people wait until placing their next order, and comment on the minimum and maximum values.

# ## Verify that the `'order_hour_of_day'` and `'order_dow'` values in the `orders` tables are sensible (i.e. `'order_hour_of_day'` ranges from 0 to 23 and `'order_dow'` ranges from 0 to 6)

# In[24]:


# Verify that values in the 'order_hour_of_day' and 'order_dow' columns are sensible
print(orders['order_hour_of_day'].describe())
print(orders['order_dow'].describe())


# ## What time of day do people shop for groceries? 
# 
# Create a plot that shows how many people place orders for each hour of the day.

# In[25]:


# Create a plot that shows how many people place orders for each hour of the day
orders['order_hour_of_day'].value_counts().plot(kind='bar')
plt.title('Orders by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')
plt.show()


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
# 
# It is better after each section, graph (or series of tests) to write a conclusion on the obtained data taking into account the set business task - so it is easier to read the project, because future colleagues or customers will not have to interpret the results of each section, test or graph themselves.

# The conclusion here is that a majority of orders in that year occurred after between 9 AM and 6 PM with most of the orders coming in around the noon hour.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №3__
# All right

# 

# ## What day of the week do people shop for groceries?
# 
# Create a plot that shows what day of the week people shop for groceries.

# In[26]:


# Create a plot that shows what day of the week people shop for groceries
orders['order_dow'].value_counts().plot(kind='bar')
plt.title('Orders by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Orders')
plt.show()


# This concludes that some instacart shopper prefer shopping on Sundays and Mondays, however it is likely that this is not stastically significant. So, it appears that orders are dispersed evenly throughout the week.

# 

# ## How long do people wait until placing another order?
# 
# Create a plot that shows how long people wait until placing their next order, and comment on the minimum and maximum values.

# In[27]:


# Create a plot that shows how long people wait until placing their next order
orders['days_since_prior_order'].plot(kind='hist')
plt.title('Days Since Prior Order')
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.show()


# The insight here is that most people reoder within 14 days with a subset reordering monthly.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №2__
# 
# You're right to sign the charts

# # Step 3B:  Create visualizations to provide the following data insights.
# 
# [B] (must complete all to pass)
# 1.	Is there a difference in 'order_hour_of_day' distributions on Wednesdays and Saturdays? Plot the histograms for both days on the same plot and describe the differences that you see.
# 2.	Plot the distribution for the number of orders that customers place (e.g. how many customers placed only 1 order, how many placed only 2, how many only 3, and so on…)
# 3.	What are the top 20 products that are ordered most frequently (display their id and name)?

# ## Is there a difference in `'order_hour_of_day'` distributions on Wednesdays and Saturdays? Plot the histograms for both days and describe the differences that you see.
# 
# Plot the histograms for both days on the same plot and describe the differences that you see.

# In[28]:


wednesdays = orders[orders['order_dow'] == 2]
saturdays = orders[orders['order_dow'] == 5]

plt.hist(wednesdays['order_hour_of_day'], alpha=0.5, label='Wednesdays')
plt.hist(saturdays['order_hour_of_day'], alpha=0.5, label='Saturdays')
plt.title('Order Hour of Day on Wednesdays and Saturdays')
plt.xlabel('Hour of Day')
plt.ylabel('Frequency')
plt.legend()
plt.show()


# The conclusion is that there is not a difference between the order hours of day on Wednesdays or Saturdays

# ## What's the distribution for the number of orders per customer?
# 
# Plot the distribution for the number of orders that customers place (e.g. how many customers placed only 1 order, how many placed only 2, how many only 3, and so on…)

# In[29]:


# Plot the distribution for the number of orders that customers place

orders.groupby('user_id')['order_id'].count().value_counts().plot(kind='bar')
plt.title('Number of Orders per Customer')
plt.xlabel('Number of Orders')
plt.ylabel('Frequency')
plt.show()


# A conclusion here would be that most customers did not order more than three times that year.

# ## What are the top 20 popular products (display their id and name)?
# 
# What are the top 20 products that are ordered most frequently (display their id and name)?

# In[30]:


# What are the top 20 products that are ordered most frequently?

top_products = order_products.groupby('product_id')['order_id'].count().sort_values(ascending=False).head(20)
top_products = top_products.reset_index()
top_products = pd.merge(top_products, products, on='product_id')
top_products.columns = ['product_id', 'order_count', 'product_name', 'aisle_id', 'department_id']
print(top_products[['product_id', 'product_name', 'order_count']])


# # Step 3C:  Create visualizations to provide the following data insights.
# 
# [C] (must complete at least two to pass)
# 1.	How many items do people typically buy in one order? What does the distribution look like?
# 2.	What are the top 20 items that are reordered most frequently (display their names and product IDs)?
# 3.	For each product, what proportion of its orders are reorders (create a table with columns for the product ID, product name, and reorder proportion)?
# 4.	For each customer, what proportion of their products ordered are reorders?
# 5.	What are the top 20 items that people put in their carts first (display the product IDs, product names, and number of times they were the first item added to the cart)?
# 

# ## How many items do people typically buy in one order? What does the distribution look like?

# In[31]:


# How many items do people typically buy in one order? What does the distribution look like?

order_products.groupby('order_id')['product_id'].count().plot(kind='hist')
plt.title('Number of Items per Order')
plt.xlabel('Number of Items')
plt.ylabel('Frequency')
plt.show()


# ## What are the top 20 items that are reordered most frequently (display their names and product IDs)?

# In[32]:


# What are the top 20 items that are reordered most frequently?

reordered_products = order_products.groupby('product_id')['reordered'].sum().sort_values(ascending=False).head(20)

reordered_products = reordered_products.reset_index()
reordered_products = pd.merge(reordered_products, products, on='product_id')
reordered_products.columns = ['product_id', 'eorder_count', 'product_name', 'aisle_id', 'department_id']

print(reordered_products[['product_id', 'product_name', 'eorder_count']])


# ## For each product, what proportion of its orders are reorders?

# In[33]:


# For each product, what proportion of its orders are reorders?

temp = order_products.groupby('product_id')['reordered'].mean().reset_index()

temp.columns = ['product_id', 'reorder_proportion']

reorder_proportions = pd.merge(temp, products, on='product_id')

print(reorder_proportions[['product_id', 'product_name', 'reorder_proportion']])


# ## For each customer, what proportion of their products ordered are reorders?

# In[34]:


temp = pd.merge(orders, order_products, on='order_id')
temp = temp.groupby(['user_id', 'product_id'])['reordered'].sum().reset_index()
temp = pd.merge(temp, products, on='product_id')
temp.columns = ['user_id', 'product_id', 'reorder_count', 'product_name', 'aisle_id', 'department_id']
customer_reorder_proportions = temp.groupby('user_id')['reorder_count'].sum() / temp.groupby('user_id')['product_id'].count()
print(customer_reorder_proportions)


# ## What are the top 20 items that people put in their carts first? 

# In[35]:


#sort
order_products_sorted = order_products.sort_values(['order_id', 'add_to_cart_order'])

#new df
first_items = order_products_sorted[order_products_sorted['add_to_cart_order'] == 1]

#rank of first items
product_counts = first_items['product_id'].value_counts()

#subset of first items
top_20_products = product_counts.nlargest(20).reset_index()

#subset with product names
top_20_products.columns = ['product_id', 'count']
top_20_products = pd.merge(top_20_products, products, on='product_id')
top_20_products = top_20_products[['product_id', 'product_name', 'count']]
top_20_products.columns = ['Product ID', 'Product Name', 'Count']

print(top_20_products)


# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
# 
# 
# It would be nice to add an overall output for the projec
# </div>

# The overall output of the project was a powerful analysis of consumer behavior at instacart. We not only analyzed their shopping habits in terms of days of the week, hours of day, and orders per year, but we also determined what the most popular products are based on reorders.

# # Congratulations! Excellent job.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №3__
# 
# 
# Otherwise it's great😊. Your project is begging for github =)   
#     
# Congratulations on the successful completion of the project 😊👍
# And I wish you success in new works 😊
