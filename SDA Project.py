#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid green 2px; padding: 20px">
#     
# <b>Hello, Nicholas!</b> We're glad to see you in code-reviewer territory. You've done a great job on the project, but let's get to know each other and make it even better! We have our own atmosphere here and a few rules:
# 
# 
# 1. I work as a code reviewer, and my main goal is not to point out your mistakes, but to share my experience and help you become a data analyst.
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

# # Which one is a better plan?
# 
# You work as an analyst for the telecom operator Megaline. The company offers its clients two prepaid plans, Surf and Ultimate. The commercial department wants to know which of the plans brings in more revenue in order to adjust the advertising budget.
# 
# You are going to carry out a preliminary analysis of the plans based on a relatively small client selection. You'll have the data on 500 Megaline clients: who the clients are, where they're from, which plan they use, and the number of calls they made and text messages they sent in 2018. Your job is to analyze the clients' behavior and determine which prepaid plan brings in more revenue.

# [We've provided you with some commentary to guide your thinking as you complete this project. However, make sure to remove all the bracketed comments before submitting your project.]
# 
# [Before you dive into analyzing your data, explain for yourself the purpose of the project and actions you plan to take.]
# 
# [Please bear in mind that studying, amending, and analyzing data is an iterative process. It is normal to return to previous steps and correct/expand them to allow for further steps.]

# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# An excellent practice is to describe the goal and main steps in your own words (a skill that will help a lot on a final project). It would be good to add the progress and purpose of the study.

# ## Initialization

# First, get ready for the worflow/pipeline by importing the relevant libraries you will need to process, analyze, and visualize the data.

# In[1]:


# Loading all the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# ## Load data

# Second, load the Megaline data for the assignment.

# In[2]:


# Load the data files into different DataFrames

calls = pd.read_csv('/datasets/megaline_calls.csv')
internet = pd.read_csv('/datasets/megaline_internet.csv')
messages = pd.read_csv('/datasets/megaline_messages.csv')
plans = pd.read_csv('/datasets/megaline_plans.csv')
users = pd.read_csv('/datasets/megaline_users.csv')


# ## Prepare the data

# In this section you will need to: (1) convert the dat at to the necessary types, (2) find and eliminate errors in the data, and (3) explain what errors you found and how you removed them.
# 
# In addition, you will need to find: (1) the number of calls made and minutes used per month, (2) the number of text messages sent per month, (3) the volume of data per month, (4) the monthly revenue from each user.
# 
# Join the output into a new table on the variable 'user_id'.
# 
# As a value-add, I have created a relationship diagram has been prepared for this assignment to facilitate coding and debugging. Please visit: https://drive.google.com/file/d/1N8DI_SQSruf5jT9vNzrq82CycF93tPZC/view?usp=sharing.

# 

# ### Plans

# In[3]:


# Print the general/summary information about the 'plans' dataframe

plans.info(show_counts=True)


# In[4]:


# Print a sample of data for plans

display(plans.head(5))


# This is a challenging data frame type because it has less rows and more columns which was not typical of previous project but better represents datasets encountered and enriched in the real world. My initial hypothesis is that this table will be used to pull information from through joining, however the linkage to be used are not initially clear.
# 
# I anticipate the floats for usd_per_message and usd_per_minute adding complexity to the visualizations, however I will encounter this later on. The basic insight I can gather here is that there are two plans a low and a high that can be characterized based on messages_included, mb_per_month or minutes_per_month otherwise categorized as 'data'.
# 
# There is no data missing in this table.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# 
# I agree

# #### Fix data

# This data set has no obvious fixes because there are only 2 rows of data and it is to describe the plan contents. I am including two fixes from the last assignment just for thoroughness. The dataset is complete in terms of non-null counts, so I don't think this is needed. The .info() also shows the data types, but the last assignment required the int64 to .astype(int) fix.

# In[5]:


#Check that integer data will be processed as an integer data type
#Remove 100% true duplicates from the dataframe

plans['messages_included'] = plans['messages_included'].astype(int)
plans['mb_per_month_included'] = plans['mb_per_month_included'].astype(int)
plans['minutes_included'] = plans['minutes_included'].astype(int)
plans['usd_monthly_pay'] = plans['usd_monthly_pay'].astype(int)
plans['usd_per_gb'] = plans['usd_per_gb'].astype(int)
plans['usd_per_minute'] = plans['usd_per_minute'].astype(int)

plans.drop_duplicates(inplace=True)


# #### Enrich data

# The plans dataframe does not need enrichment at this time.

# ### Users

# In[6]:


# Print the general/summary information about the 'users' dataframe

users.info(show_counts = True)


# In[7]:


# Print a sample of data for users

display(users.head(5))


# In this dataset we see descriptive information of users of either either the surf or ultimate plan in the U.S. user_id will be a critical data field and others will be used in right joins to add more information. 
# 
# 'reg_date' is always a tricky data type, so I will need to address this upon the first error. Additionally, the 'churn_date' column does not make complete sense upon first review. I also see that the string or object in the 'city' column may be an issue if it needs to pull through at this point. The state information is useful and county information would need significant enrichment. The MSA text seems superfluous.
# 
# The date issue can be fixed by a valid transformation likely in pandas. The data in the city column can either be stripped or parsed into new columns or an entirely new dataframe.

#  

# #### Fix Data

# This data set has no obvious fixes because it is a dataframe that contains customer information as opposed to the utilization. I can see that we are moving towards the merge. I am including two fixes from the last assignment just for thoroughness. The dataset is complete in terms of non-null counts, so I don't think these two fixes are even needed. The .info() also shows the data types, but the last assignment required the int64 to .astype(int) fix.

# In[8]:


#Check that integer data will be processed as an integer data type
#Remove 100% true duplicates from the dataframe
#Convert date data type into a pandas readable format

users['user_id'] = users['user_id'].astype(int)
users['age'] = users['age'].astype(int)

users.drop_duplicates(inplace=True)

users['reg_date'] = pd.to_datetime(users['reg_date'])
users['churn_date'] = pd.to_datetime(users['churn_date'], errors='coerce')


# #### Enrich Data

# The operation here is to extract months from the date column.

# In[9]:


# Extract month from call date

users['reg_month'] = users['reg_date'].dt.month

users['churn_month'] = users['churn_date'].dt.month


# ## Calls

# In[10]:


# Print the general/summary information about the 'calls' dataframe

calls.info(show_counts = True)


# In[11]:


# Print a sample of data for calls

display(calls.head(5))


# The critical piece of information in this table is the 'duration' column. I think that it will be used for value_counts() on the user_id column to get a sum of minutes spent using the 'duration' column. The 'id' and 'call_date' columns don't appear to have that much value at this time thinking ahead. Similarly to the last set of dates, I think the format will be an issue if these data are used perhaps if a monthly, quarterly, annual request is made. This can be fixed by a valid transformation likely in pandas.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# 
# Great. First look at the data is done

#  

# #### Fix data

# This data set has no obvious fixes. The dataset is complete in terms of non-null counts.

# In[12]:


#Check that integer data will be processed as an integer data type
#Remove 100% true duplicates from the dataframe
#Convert date data type into a pandas readable format

calls['user_id'] = calls['user_id'].astype(int)

calls.drop_duplicates(inplace=True)

calls['call_date'] = pd.to_datetime(calls['call_date'])


# #### Enrich data

# The operation here is to extract months from the date column

# In[13]:


# Extract month from call date

calls['month'] = calls['call_date'].dt.month

calls['duration'] = np.ceil(calls['duration'])


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# At the end of each call, the duration of the call is rounded up. The `np.ceil()` method should be used.

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
# 
# The variable calls has not been reassigned after using np.ceil(calls['duration']). To fix this, the student should use the following code:
#     
#     calls['duration'] = np.ceil(calls['duration'])
# 

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №3__
# 
# Now correct

# ## Messages

# In[14]:


# Print the general/summary information about the 'messages' dataframe

messages.info(show_counts = True)


# In[15]:


# Print a sample of data for 'messages'

display(messages.head(5))


# I see similar potential calculations in this table as what was described in the calls dataframe. I think there will be a simpler count needed here to determine the number of messages sent over a period of time. I don't anticipate any issues other than the date format. This can be fixed by a valid transformation likely in pandas.

#  

# #### Fix data

# No obvious fixes. Same as previously mentioned.

# In[16]:


#Check that integer data will be processed as an integer data type
#Remove 100% true duplicates from the dataframe
#Convert date data type into a pandas readable format

messages['user_id'] = messages['user_id'].astype(int)

messages.drop_duplicates(inplace=True)

messages['message_date'] = pd.to_datetime(messages['message_date'])


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Duplicate checking is the basis of data preprocessing

# #### Enrich data

# The operation here is to extract months from the date column

# In[17]:


# Extract month from call date

messages['month'] = messages['message_date'].dt.month


# ## Internet

# In[18]:


# Print the general/summary information about the 'internet' dataframe

internet.info(show_counts = True)


# In[19]:


# Print a sample of data for the internet traffic

display(internet.head(5))


# I see similar potential calculations in this table as what was described in the calls and messages dataframe. I think there will be a simpler count needed here to determine the number of messages sent over a period of time. 
# 
# I don't anticipate any issues other than the date format. This can be fixed by a valid transformation likely in pandas. I also suspect that mb_used will be rounded up which may the issue of reconciling whether it triggers at >n.0 or >n.5.

#  

# #### Fix data

# No obvious fixes. Same as previously mentioned.

# In[20]:


#Check that integer data will be processed as an integer data type
#Remove 100% true duplicates from the dataframe
#Convert date data type into a pandas readable format

internet['user_id'] = internet['user_id'].astype(int)

internet.drop_duplicates(inplace=True)

internet['month'] = pd.to_datetime(internet['session_date']).dt.month

display(internet)


# The operation here is to extract months from the date column

# #### Enrich data

# 

# ## Study plan conditions

# In[21]:


# Print out the plan conditions and make sure they are clear for you

display(plans)


# ## Aggregate data per user
# 

# In[22]:


# Calculate the number of calls made by each user per month. Save the result.

calls_per_month = calls.groupby(['user_id', 'month'])['month'].count().reset_index(name='calls_per_month')

display(calls_per_month)


# In[23]:


# Calculate the amount of minutes spent by each user per month. Save the result.

minutes_per_month = calls.groupby(['user_id', 'month'])['duration'].sum().reset_index(name='minutes_per_month')

display(minutes_per_month)


# In[24]:


# Calculate the number of messages sent by each user per month. Save the result.

messages_per_month = messages.groupby(['user_id', 'month'])['month'].count().reset_index(name='messages_per_month')

display(messages_per_month)


# In[25]:


# Calculate the volume of internet traffic used by each user per month. Save the result.

display(internet.columns)

internet_traffic_per_month = internet.groupby(['user_id', 'month'])['mb_used'].sum().reset_index(name='internet_traffic_per_month')


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# 
# It is better to use display() rather than print() to output a dataframe object. This way it will be clearer

# In[26]:


# Merge calls_per_month, minutes_per_month, messages_per_month, and internet_traffic_per_month
merged_data = pd.merge(calls_per_month, minutes_per_month, on=['user_id', 'month'], how='outer')
merged_data = pd.merge(merged_data, messages_per_month, on=['user_id', 'month'], how='outer')
merged_data = pd.merge(merged_data, internet_traffic_per_month, on=['user_id', 'month'], how='outer')

display(merged_data)


# In[27]:


# Create a new column in merged_data for user_ids with plan 'surf' or 'ultimate'
# Merge users and merged_data dataframes on user_id

merged_data = pd.merge(merged_data, users[['user_id', 'plan']], on='user_id', how='left')

display(merged_data)


# Calculate the monthly revenue from each user (subtract the free package limit from the total number of calls, text messages, and data; multiply the result by the calling plan value; add the monthly charge depending on the calling plan). Recall the initial "free package" details from the project description.

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
# 
# Some blocks of code are not working. Please see what went wrong. Before submitting a project, you should check if the code works - you can do this by clicking on the Jupiter Hub Kernel and Restart & Run All panels
# 

# In[28]:


# Calculate the monthly revenue for each user

def calculate_revenue(row):
    if row['plan'] == 'surf':
        minutes_cost = max(0, row['minutes_per_month'] - 500) * 0.03
        messages_cost = max(0, row['messages_per_month'] - 50) * 0.03
        data_cost = max(0, np.ceil(row['internet_traffic_per_month'] / 1024) - 15) * 10
        return 20 + minutes_cost + messages_cost + data_cost
    elif row['plan'] == 'ultimate':
        minutes_cost = max(0, row['minutes_per_month'] - 3000) * 0.01
        messages_cost = max(0, row['messages_per_month'] - 1000) * 0.01
        data_cost = max(0, np.ceil(row['internet_traffic_per_month'] / 1024) - 30) * 7
        return 70 + minutes_cost + messages_cost + data_cost
    else:
        return 0  # or some other default value

merged_data['revenue'] = merged_data.apply(calculate_revenue, axis=1)

print(merged_data['revenue'])


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# That's right. There are 1,024 megabytes in one gigabyte.

# ## Study user behaviour

# The workflow that I have developed based on an improvement of the project description is the following: (1) perform descriptive statistics on metrics for usage across all users, (2) calculate the average usage in each month by plan and round, (3) split the average usage metrics into individual dataframes based on plan, (4) calculate totals and round, (5) plot total usage per month as a bar chart, (6) plot usage by cumulative users, (7) calculate the mean and variance for the split dataframes and round, and lastly (8) create a boxplot using the outputs from 7 and judge whether the insights match the statistics.

# ### Calls

# In[29]:


#Descriptive Statistics

print(merged_data.groupby('plan')['calls_per_month'].describe())
print(merged_data.groupby('plan')['minutes_per_month'].describe())
print(merged_data.groupby('plan')['messages_per_month'].describe())
print(merged_data.groupby('plan')['internet_traffic_per_month'].describe())


# In[30]:


# Calculate the average duration of calls per each plan per each distinct month

# Merge the users dataframe with the calls dataframe on the user_id column
call_duration_plan_data = calls.merge(users[['user_id', 'plan']], on='user_id', how='left')

# Calculate the average duration of calls per each plan per each distinct month
avg_duration = call_duration_plan_data.groupby(['plan', 'month'])['duration'].mean().reset_index()

print(avg_duration)


# In[31]:


# Filter the data for the 'surf' and 'ultimate' plans

surf_call_data = call_duration_plan_data[call_duration_plan_data['plan'] == 'surf']

print(surf_call_data)

# Filter the data for the 'ultimate' plan
ultimate_call_data = call_duration_plan_data[call_duration_plan_data['plan'] == 'ultimate']

print(ultimate_call_data)


# In[32]:


# Calculate the total duration of calls for the 'surf' plan
total_surf_duration = surf_call_data['duration'].sum()

total_surf_duration = round(total_surf_duration, 1)

print('Based on Megaline data from 2018, the total duration of calls in a year for surf plan Megaline customers is: ', total_surf_duration, 'minutes.')
print('Based on Megaline data from 2018, the total duration of calls in a month for surf plan Megaline customers is: ', total_surf_duration / 12, "minutes.")


# Calculate the total duration of calls for the 'ultimate' plan
total_ultimate_duration = ultimate_call_data['duration'].sum()

total_ultimate_duration = round(total_ultimate_duration, 1)

print('Based on Megaline data from 2018, the total duration of calls in a year for ultimate plan Megaline customers is: ', total_ultimate_duration, 'minutes.')
print('Based on Megaline data from 2018, the total duration of calls in a month for ultimate plan Megaline customers is: ', total_surf_duration / 12, 'minutes.')


# In[33]:


# Create a new figure
plt.figure(figsize=(10, 6))

# Create a stacked bar plot
sns.barplot(x='month', y='duration', hue='plan', data=pd.concat([surf_call_data, ultimate_call_data]))

# Set the x-axis label
plt.xlabel('Month')

# Set the y-axis label
plt.ylabel('Total Duration')

# Set the title
plt.title('Total Duration of Calls by Month and Plan')

# Show the plot
plt.show()


# In[34]:


# Create a new figure
plt.figure(figsize=(10, 6))

# Create an overlapping histogram
sns.histplot(surf_call_data['duration'], label='Surf', alpha=0.5, color='blue')
sns.histplot(ultimate_call_data['duration'], label='Ultimate', alpha=0.5, color='red')

# Set the x-axis label
plt.xlabel('Duration')

# Set the y-axis label
plt.ylabel('Frequency')

# Set the title
plt.title('Histogram of Call Durations by Plan')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[35]:


# Calculate the mean and variance of the monthly call duration
mean_duration = pd.concat([surf_call_data, ultimate_call_data])['duration'].mean()
var_duration = pd.concat([surf_call_data, ultimate_call_data])['duration'].var()

# Round the mean and variance to one decimal place
mean_duration = round(mean_duration, 1)
var_duration = round(var_duration, 1)

# Print the mean and variance
print('Mean duration:', mean_duration, 'minutes')
print('Variance duration:', var_duration, 'minutes')


# In[36]:


# Plot a boxplot to visualize the distribution of the monthly call duration
plt.figure(figsize=(10, 6))
plt.boxplot(pd.concat([surf_call_data, ultimate_call_data])['duration'])
plt.title('Boxplot of Monthly Call Duration')

plt.ylabel('Minutes')
plt.show()


# In 2018, Megaline customers’ call durations ranged from 6.2 to 6.9 minutes per month across both plan types with a mean of 6.7 minutes. Variance was high as demonstrated in the box plot mainly due to the presence of outliers. Differences in the average call durations between Surf and Ultimate plan customers are likely not statistically significant month-to-month. Total call durations were 636,691 minutes for Megaline’s Surf plan customers and 292,459 minutes for Megaline’s Ultimate plan customers. The histogram demonstrates that Surf plan customers are making a higher volume of calls, especially those under 1 minute when compared to the Ultimate plan customers during the same period of 2018.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Great visualization

#  

# ### Messages

# In[37]:


# Compare the number of messages users of each plan tend to send each month

# Merge the users dataframe with the calls dataframe on the user_id column
message_sum_plan_data = messages_per_month.merge(users[['user_id', 'plan']], on='user_id', how='left')

print(message_sum_plan_data)


# In[38]:


# Calculate the mean number of messages sent by users of each plan
avg_messages = message_sum_plan_data.groupby(['plan', 'month'])['messages_per_month'].mean().reset_index()

avg_messages = round(avg_messages, 1)

print(avg_messages)


# In[39]:


# Filter the data for the 'surf' and 'ultimate' plans

surf_message_data = message_sum_plan_data[message_sum_plan_data['plan'] == 'surf']

print(surf_message_data)

# Filter the data for the 'ultimate' plan
ultimate_message_data = message_sum_plan_data[message_sum_plan_data['plan'] == 'ultimate']

print(ultimate_message_data)


# In[40]:


# Calculate the total number of messages for the 'surf' plan
total_surf_messages = surf_message_data['messages_per_month'].sum()

total_surf_messages = round(total_surf_messages, 1)

print('Based on Megaline data from 2018, the total duration of calls in a year for surf plan Megaline customers is: ', total_surf_messages, 'minutes.')
print('Based on Megaline data from 2018, the total duration of calls in a month for surf plan Megaline customers is: ', total_surf_messages / 12, "minutes.")


# Calculate the total number of messages for the 'ultimate' plan
total_ultimate_messages = ultimate_message_data['messages_per_month'].sum()

total_ultimate_messages = round(total_ultimate_messages, 1)

print('Based on Megaline data from 2018, the total duration of calls in a year for ultimate plan Megaline customers is: ', total_ultimate_messages, 'minutes.')
print('Based on Megaline data from 2018, the total duration of calls in a month for ultimate plan Megaline customers is: ', total_ultimate_messages / 12, 'minutes.')


# In[41]:


# Create a new figure
plt.figure(figsize=(10, 6))

# Create a stacked bar plot
sns.barplot(x='month', y='messages_per_month', hue='plan', data=pd.concat([surf_message_data, ultimate_message_data]))

# Set the x-axis label
plt.xlabel('Month')

# Set the y-axis label
plt.ylabel('Total Number of Messages')

# Set the title
plt.title('Total Number of Messages by Month and Plan')

# Show the plot
plt.show()


# In[42]:


# Create a new figure
plt.figure(figsize=(10, 6))

# Create an overlapping histogram
sns.histplot(surf_message_data['messages_per_month'], label='Surf', alpha=0.5, color='blue')
sns.histplot(ultimate_message_data['messages_per_month'], label='Ultimate', alpha=0.5, color='red')

# Set the x-axis label
plt.xlabel('Number of Messages')

# Set the y-axis label
plt.ylabel('Number of Users')

# Set the title
plt.title('Histogram of the Number of Messages by Plan')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[43]:


# Calculate the mean and variance of the monthly call duration
mean_monthly_messages = pd.concat([surf_message_data, ultimate_message_data])['messages_per_month'].mean()
var_monthly_messages = pd.concat([surf_message_data, ultimate_message_data])['messages_per_month'].var()

# Round the mean and variance to one decimal place
mean_monthly_messages = round(mean_monthly_messages, 1)
var_monthly_messages = round(var_monthly_messages, 1)

# Print the mean and variance
print('Mean duration:', mean_monthly_messages, 'messages')
print('Variance duration:', var_monthly_messages, 'messages')


# In[44]:


# Plot a boxplot to visualize the distribution of the monthly call duration
plt.figure(figsize=(10, 6))
plt.boxplot(pd.concat([surf_message_data, ultimate_message_data])['messages_per_month'])
plt.title('Boxplot of Messages per Month')
plt.ylabel('Number of Messages')
plt.show()


# Megaline customers’ messages sent ranged from 21 to 54 messages per month across both plan types with a mean of 42.1 messages. Similar to the call duration data, variance in the number of messages sent per month was high as demonstrated in the box plot mainly due to the presence of outliers. The total number of messages was 49,014 for Surf plan customers and 27,037 for Ultimate plan users. The bar chart suggests that there may be a difference between the average number of messages sent from Ultimate plan customers compared to Surf plan users during the same period of 2018. However, this is not the case when interpreting the result of the histogram.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# All right

#  

# ### Internet
# 
# Compare the amount of internet traffic consumed by users per plan

# In[45]:


# Merge the users dataframe with the calls dataframe on the user_id column
mb_sum_plan_data = internet.merge(users[['user_id', 'plan']], on='user_id', how='left')

print(mb_sum_plan_data)


# In[46]:


# Calculate the mean number of messages sent by users of each plan

avg_internet = mb_sum_plan_data.groupby(['plan', 'month'])['mb_used'].mean().reset_index()

print(avg_internet)


# In[47]:


# Filter the data for the 'surf' and 'ultimate' plans

surf_internet_data = mb_sum_plan_data[mb_sum_plan_data['plan'] == 'surf']

print(surf_internet_data)

# Filter the data for the 'ultimate' plan
ultimate_internet_data = mb_sum_plan_data[mb_sum_plan_data['plan'] == 'ultimate']

print(ultimate_internet_data)


# In[48]:


# Calculate the total amount of internet consumed for the 'surf' plan
total_surf_internet = surf_internet_data['mb_used'].sum()

total_surf_internet = round(total_surf_internet, 1)

print('Based on Megaline data from 2018, the total amount of internet consumed in a year for surf plan Megaline customers is: ', total_surf_internet, 'megabytes.')
print('Based on Megaline data from 2018, the total amount of internet consumed in a month for surf plan Megaline customers is: ', round((total_surf_internet / 12), 1), "megabytes.")


# Calculate the total amount of internet consumed for the 'ultimate' plan
total_ultimate_internet = ultimate_internet_data['mb_used'].sum()

total_ultimate_internet = round(total_ultimate_internet, 1)

print('Based on Megaline data from 2018, the total amount of internet consumed in a year for ultimate plan Megaline customers is: ', total_ultimate_internet, 'megabytes.')
print('Based on Megaline data from 2018, the total amount of internet consumed in a month for ultimate plan Megaline customers is: ', round((total_ultimate_internet / 12),1), 'megabytes.')


# In[49]:


# Create a new figure
plt.figure(figsize=(10, 6))

# Create a stacked bar plot
sns.barplot(x='month', y='mb_used', hue='plan', data=pd.concat([surf_internet_data, ultimate_internet_data]))

# Set the x-axis label
plt.xlabel('Month')

# Set the y-axis label
plt.ylabel('Total Amount of Internet Consumed (Mb)')

# Set the title
plt.title('Total Number of Messages by Month and Plan')

# Show the plot
plt.show()


# In[50]:


# Create a new figure
plt.figure(figsize=(10, 6))

# Create an overlapping histogram
sns.histplot(surf_internet_data['mb_used'], label='Surf', alpha=0.5, color='blue')
sns.histplot(ultimate_internet_data['mb_used'], label='Ultimate', alpha=0.5, color='red')

# Set the x-axis label
plt.xlabel('Amount of Internet Consumed (Mb)')

# Set the y-axis label
plt.ylabel('Number of Users')

# Set the title
plt.title('Histogram of the Amount of Internet Consumed by Plan')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[51]:


# Calculate the mean and variance of the monthly call duration
mean_monthly_internet = pd.concat([surf_internet_data, ultimate_internet_data])['mb_used'].mean()
var_monthly_internet = pd.concat([surf_internet_data, ultimate_internet_data])['mb_used'].var()

# Round the mean and variance to one decimal place
mean_monthly_internet = round(mean_monthly_internet, 1)
var_monthly_internet = round(var_monthly_internet, 1)

# Print the mean and variance
print('Mean Mb used:', mean_monthly_internet, 'megabytes')
print('Variance Mb used:', var_monthly_internet, 'megabytes')


# In[52]:


# Plot a boxplot to visualize the distribution of the monthly call duration
plt.figure(figsize=(10, 6))
plt.boxplot(pd.concat([surf_internet_data, ultimate_internet_data])['mb_used'])
plt.title('Boxplot of Internet Consumed per Month')
plt.ylabel('Internet Consumed (Mb)')
plt.show()


# Next, Megaline customers’ monthly internet usage ranged from 325.0 to 419.3 Mb per month across both plan types with a mean of 6.7 minutes. The variance was high as demonstrated in the box plot mainly due to the presence of outliers. Differences in the average internet usage between Surf and Ultimate plan customers are likely not statistically significant month-to-month. Total internet usage was 26,046,179.9 Mb for Megaline’s Surf plan customers and 12,394,583.8 Mb for Megaline’s Ultimate plan customers. The histogram demonstrates that Surf plan customers are consuming greater amounts of internet annually, which strongly suggests that there is a difference in consumption rates between these two groups in this year.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Well done

#  

# ## Revenue

# [Likewise you have studied the user behaviour, statistically describe the revenue between the plans.]

# In[53]:


# Calculate the mean number of messages sent by users of each plan

avg_revenue = merged_data.groupby(['plan', 'month'])['revenue'].mean().reset_index()

avg_revenue = round(avg_revenue, 1)

print(avg_revenue)


# In[54]:


# Filter the data for the 'surf' and 'ultimate' plans

surf_revenue_data = merged_data[merged_data['plan'] == 'surf']

print(surf_revenue_data)

# Filter the data for the 'ultimate' plan
ultimate_revenue_data = merged_data[merged_data['plan'] == 'ultimate']

print(ultimate_revenue_data)


# In[55]:


# Calculate the total amount of internet consumed for the 'surf' plan
total_surf_revenue = surf_revenue_data['revenue'].sum()

total_surf_revenue = round(total_surf_revenue, 2)

print('Based on Megaline data from 2018, the revenue in a year from surf plan Megaline customers is: ', total_surf_revenue, 'USD.')
print('Based on Megaline data from 2018, the revenue in a month from surf plan Megaline customers is: ', round((total_surf_revenue / 12), 2), "USD.")


# Calculate the total amount of internet consumed for the 'ultimate' plan
total_ultimate_revenue = ultimate_revenue_data['revenue'].sum()

total_ultimate_revenue = round(total_ultimate_revenue, 2)

print('Based on Megaline data from 2018, the revenue in a year from ultimate plan Megaline customers is: ', total_ultimate_revenue, 'USD.')
print('Based on Megaline data from 2018, the revenue in a month for ultimate plan Megaline customers is: ', round((total_ultimate_revenue / 12),2), 'USD.')


# In[56]:


# Create a new figure
plt.figure(figsize=(10, 6))

# Create a stacked bar plot
sns.barplot(x='month', y='revenue', hue='plan', data=pd.concat([surf_revenue_data, ultimate_revenue_data]))

# Set the x-axis label
plt.xlabel('Month')

# Set the y-axis label
plt.ylabel('Total Revenue (USD))')

# Set the title
plt.title('Total Revenue by Month and Plan')

# Show the plot
plt.show()


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# All necessary libraries should be unloaded at the beginning of the project in one code cell

# In[57]:


# Create a new figure
plt.figure(figsize=(10, 6))

# Create an overlapping histogram
sns.histplot(surf_revenue_data['revenue'], label='Surf', alpha=0.5, color='blue')
sns.histplot(ultimate_revenue_data['revenue'], label='Ultimate', alpha=0.5, color='red')

# Set the x-axis label
plt.xlabel('Amount of Revenue (USD)')

# Set the y-axis label
plt.ylabel('Number of Users')

# Set the title
plt.title('Histogram of the Revenue by Plan')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[58]:


# Calculate the mean and variance of the monthly call duration
mean_monthly_revenue = pd.concat([surf_revenue_data, ultimate_revenue_data])['revenue'].mean()
var_monthly_revenue = pd.concat([surf_revenue_data, ultimate_revenue_data])['revenue'].var()

# Round the mean and variance to one decimal place
mean_monthly_revenue = round(mean_monthly_revenue, 2)
var_monthly_revenue = round(var_monthly_revenue, 2)

# Print the mean and variance
print('Mean revenue:', mean_monthly_revenue, 'USD')
print('Variance revenue:', var_monthly_revenue, 'USD')


# In[59]:


# Plot a boxplot to visualize the distribution of the monthly call duration
plt.figure(figsize=(10, 6))
plt.boxplot(pd.concat([surf_revenue_data, ultimate_revenue_data])['revenue'])
plt.title('Boxplot of Revenue')
plt.ylabel('Revenue (USD)')
plt.show()


# Lastly, Megaline’s monthly revenue per customers ranged from $20.0 to $73.4  across both plan types with a mean of $64.09. 
# 
# The variance was high as demonstrated in the box plot mainly due to the presence of outliers. 
# 
# There is a clear difference in monthly revenue by plan.
# 
# Total revenue was $94,894.92 among Megaline’s Surf plan customers and $52,066.00 among Megaline’s Ultimate plan customers, which is further supported by the histogram. 
# 
# The statistical test to determine whether the average revenue between Surf and Ultimate plan customers differ suggests that there is not enough information to determine whether they are different, however, all other data suggest that there is a difference. I suggest looking at the individual user revenue data to make the final conclusion.

#  

# ## Test statistical hypotheses

# The null hypothesis is that the average revenue from Surf plan customers is equa to Ultimate plan customers. The alternative hypothesis is that there is a statistically significant difference between the two groups. The proper statistical test is a two-sample, two-sided student's t-test because the directionality of the change we are trying to detect is not of importance. The alpha value is set at 0.05 to provide sufficient stringency.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №3__
# 
# Correct interpretation of the null and alternative hypotheses

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# 
# H₀(null hypothesis) is always formulated to use the equal sign(=).

# In[60]:


# Test the hypotheses

surf_revenue_data = merged_data[merged_data['plan'] == 'surf']['revenue']
ultimate_revenue_data = merged_data[merged_data['plan'] == 'ultimate']['revenue']

alpha = 0.05

results = stats.ttest_ind(surf_revenue_data, ultimate_revenue_data)

print('p-value: ', results.pvalue / 2)

if results.pvalue < alpha:
    print('Reject the null hypothesis')
else:
    print('Fail to reject the null hypothesis')


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# 
# When conducting hypothesis tests, it's crucial to test the hypotheses based on the characteristics of the data rather than pre-aggregated values. Grouping data before hypothesis testing can lead to a biased interpretation of the results. Hypothesis tests are designed to evaluate specific characteristics or relationships within the data, and grouping can introduce additional dependencies or overlook important nuances in the data.
# 
# For accurate and reliable hypothesis testing, it's recommended to work with the raw data without pre-grouping or aggregation. By directly testing the hypotheses based on the individual data points, you ensure a more robust analysis and valid conclusions that reflect the true nature of the dataset.
# 
# Therefore, for hypothesis testing, it's best to work with the original dataset without unnecessary data manipulation that may alter the outcomes of the statistical tests.
# 

# P-value << 0.05 meaning that we conclude that there is enough evidence of a difference between the datasets so that the average revenue is not equal between the two.

# [Test the hypothesis that the average revenue from users in the NY-NJ area is different from that of the users from the other regions.]

# Next, we test the he null hypothesis that there is a statistically significant difference between the average revenue from Megaline customers in New York and New Jersey compared to the rest of the country. The alternative hypothesis is that there is not a statistically significant difference between the two groups. The proper statistical test is a one-sample, two-sided student's t-test because the directionality of the change we are trying to detect is not of importance. The alpha value is set at 0.05 to provide sufficient stringency.

# In[61]:


# Extract the data for users from the NY-NJ area
ny_nj_users = users[users['city'].str.contains('NY|NJ', na=False)]

# Extract the data for users from the rest of the regions
other_users = users[~users['city'].str.contains('NY|NJ', na=False)]

other_users_sample = other_users.sample(n=len(other_users), random_state=42)

# Merge the revenue data from the merged_data dataframe into the ny_nj_users dataframe
ny_nj_users = ny_nj_users.merge(merged_data[['user_id', 'revenue']], on='user_id', how='left')

# Merge the revenue data from the merged_data dataframe into the other_users_sample dataframe
other_users_sample = other_users_sample.merge(merged_data[['user_id', 'revenue']], on='user_id', how='left')

# Handle missing values in the revenue column
ny_nj_users['revenue'] = ny_nj_users['revenue'].fillna(0)  # or use another imputation method
other_users_sample['revenue'] = other_users_sample['revenue'].fillna(0)  # or use another imputation method

# Extract the revenue columns
ny_nj_revenue = ny_nj_users['revenue']
other_revenue = other_users_sample['revenue']

# Test the hypothesis that the average revenue from users in the NY-NJ area is different from that of the users from the other regions
alpha = 0.05
results = stats.ttest_ind(ny_nj_revenue, other_revenue)

print('p-value: ', results.pvalue)

if results.pvalue < alpha:
    print('Reject the null hypothesis: The average revenue from users in the NY-NJ area is different from that of the users from the other regions.')
else:
    print('Fail to reject the null hypothesis: The average revenue from users in the NY-NJ area is not different from that of the users from the other regions.')


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# 
# Result nan - incorrect data in the hypothesis

# P-value = 0.13 > 0.05 meaning that we assume the null hypothesis is true. The statistical test to determine whether the average revenue between Surf and Ultimate plan customers in the states listed differ.

# ## General conclusion
# 
# In conclusion, Megaline is making approximately $147K annually from both of these plan types. Total internet usage was 36.4 Tb in 2018. Surf plan customers are more valuable to the overall business as they drive most of the revenue despite the Ultimate plan customers being more lucrative. Some clear differences between consumer behavior were detected with regards to call duration and messages sent. The high variance and outliers suggest that customers of both plans would benefit from higher base limits.

# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
#     
# Please correct the conclusions after correction

#  

# In[ ]:





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
