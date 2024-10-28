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

# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Please dont drop my comment!

# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Some blocks of code are not working. Please see what went wrong. Before submitting a project, you should check if the code works - you can do this by clicking on the Jupiter Hub Kernel and Restart & Run All panels ![image.png](attachment:image.png)

# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
#     
#     
# Your project is hard to read because there are no headers / comments are written in code instead of Markdown cells / no conclusions].
# 
# Please use the project layout tutorial to correct these shortcomings. 
# It can be found in the course unit
# 
# In the form of comments to the code, you should write explanations why you used certain python methods, why you grouped the data, why you need slices, etc.
# Everything else - conclusions, recommendations, decisions made, pointing out anomalies found, analyzing graphs, etc. should be written in makdown cells. This way your project will be easier to read.    
# 
# 
# ![image.png](attachment:image.png)

# 

# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
#     
#     
# It seems that the project was worked on locally and the file paths were not changed to public. It would be worth rewriting the code so that it would run both in the jupiter hub and locally without making additional edits. This can be achieved in many ways. For example, use the try-except construct for file paths: try - paths on the local computer, except - paths on the server.    
# 
# 
# ![image.png](attachment:image.png)

# In[ ]:





# # Project Description

# You work for the online store Dice, which sells video games all over the world. User and expert reviews, genres, platforms (e.g. Xbox or PlayStation), and historical data on game sales are available from open sources. You need to identify patterns that determine whether a game succeeds or not. This will allow you to spot potential big winners and plan advertising campaigns.
# 
# In front of you is data going back to 2016. Let’s imagine that it’s December 2016 and you’re planning a campaign for 2017. 
# (The important thing is to get experience working with data. It doesn't really matter whether you're forecasting 2017 sales based on data from 2016 or 2027 sales based on data from 2026.)
# 
# The dataset contains the abbreviation ESRB. The Entertainment Software Rating Board evaluates a game's content and assigns an age rating such as Teen or Mature.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# An excellent practice is to describe the goal and main steps in your own words (a skill that will help a lot on a final project). 

# ## Step 1: Initialization
# 
# ### Open the data file and study the general information
# (File path: /datasets/games.csv)

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import linregress


# In[2]:


#Please keep reading the code. I am not having issues in VS Code. Visit these two links for additional information: https://drive.google.com/file/d/1T2WyOqvxl1ohokqSDuvyuOYA9xRbORwa/view?usp=sharing and https://tripleten5.onrender.com/.
games = pd.read_csv('/datasets/games.csv')

display(games.head(5))


# 

# In[3]:


games.info()


# ## Step 2: Data Preparation

# ### Replace the column names (make them lowercase)

# In[4]:


games.columns = games.columns.str.lower()


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Great

# ### Describe the columns where the data types have been changed and why.

# ##### The data types were not modified at this point in the analysis and instead were modified to read as integers from floats or dates when a computation or hash sharding was conducted so that the root dataframe would be maintained intact.

# ### If necessary, decide how to deal with missing values:
#      a. Explain why you filled in the missing values as you did or why you decided to leave them blank.
#      b. Why do you think the values are missing? Give possible reasons.
#      c. Pay attention to the abbreviation TBD (to be determined). Specify how you intend to handle such cases.

# Missing values, NaN and 'tbd' values were dropped. I decided not to implement a centroid method, because of the skew we will be looking for later on in the analysis with different segmentations or stratifications. I think some data values were missing either through lack of collection and reporting or the game was too new of a release to have the data yet. Alternately, it could have been too old. This can be its own investigation should it be a customer requirement.

# In[5]:


#Remove NaN from name column and rows starting with hack
games = games[games['name'].notna()]
games = games[~games['name'].str.contains('.hack')]


# In[6]:


#Remove NaN from year_of_release column
games_years_clean = games.dropna(subset=['year_of_release'])


# In[7]:


# Impute NaN in critic_score with mean score for that genre
games['critic_score'].fillna(games.groupby('genre')['critic_score'].transform('mean'), inplace=True)

# Convert user_score to numeric
games['user_score'] = games['user_score'].replace('tbd', np.nan).astype(float)

# Impute NaN in user_score with mean user score for that platform
games['user_score'].fillna(games.groupby('platform')['user_score'].transform('mean'), inplace=True)


# In[8]:


# Check for non-numeric values
games['rating'] = pd.to_numeric(games['rating'], errors='coerce')

# Check for infinite values
games.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill NaN values with median
games['rating'].fillna(games.groupby('genre')['rating'].transform('mean'), inplace=True)


# 
# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Deleted 50% of the dataset, that's too much. I recommend no more than 10%

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №2__
# 
# Now correct

# In[9]:


duplicates = games.duplicated()
print(duplicates.sum())

duplicates = games.duplicated()
duplicate_rows = games[duplicates]
print(duplicate_rows)


# ### Calculate the total sales (the sum of sales in all regions) for each game and put these values in a separate column.

# In[10]:


total_games_sales = games.groupby('name')[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum().reset_index()

total_games_sales['ww_total'] = total_games_sales[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

display(total_games_sales)


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# There is no check for duplicates. Please add them.
#     
# 

# <div class="alert alert-block alert-success">✔️
# 
# __Reviewer's comment №2__
#     
# Duplicate checking is the basis of data preprocessing

# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Please, add an intermediate conclusion about this introductory part. What have been done, what hypotheses about the data do we have and what we are going to do next

# In this section, I started by importing the packages that I wanted to use. I had to revise this as I worked through the script. Next, I imported the dataset into Jupyter because I was having issues accessing the cwd from my desktop this time. Then, I went on to pre-processing by dropping rows with NaN in the ['year_of_release'] because I figured this would be the most important data field to show differences over time. There were also some rows in ['name'] that started with '.hack' so I removed these. Next, I did some significant changes to the ['user_score'], ['critic_score'], and ['rating'] columns to check for NaNs and fill them with means because I think creates a more normal distribution than medians would. Lastly, I end this on a simple two-step duplicate check and create the df for total sales. 

# <div class="alert alert-block alert-success">✔️
# 
# __Reviewer's comment №2__
#     
# I agree

# ## Step 3: Exploratory Data Analysis

# ### Look at how many games were released in different years. Is the data for every period significant?

# In[11]:


# Create a histogram of the number of games released per year
plt.figure(figsize=(18,8))
plt.hist(games['year_of_release'], bins=range(int(games['year_of_release'].min()), int(games['year_of_release'].max()+1)), align='left')
plt.xlabel('Year of Release')
plt.ylabel('Number of Games')
plt.title('Number of Games Released per Year')
plt.xticks(rotation=45)

# Add data labels
for i, v in zip(games['year_of_release'].value_counts().sort_index().index, games['year_of_release'].value_counts().sort_index().values):
    plt.text(i, v, str(v), ha='center')

plt.show()


# <div class="alert alert-block alert-warning">📝
# 
# __Reviewer's comment №1__
#     
# 
# It would be nice to add visualizations. In order to build a graph, you need to group the data (in our case, the year of release and quantity)
#     
# ![image-3.png](attachment:image-3.png)
#     
# ---
# Next, using the sns library (it's powerful, and you can do anything with it). From the data in the grouped table, plot the graph. You can have it if you want =) The main thing is to play around with the arguments and figure it out. In future projects you will build powerful graphs, this skill will come in handy there    
#     
# ![image-4.png](attachment:image-4.png)
# </div>

# In[12]:


games_sales = games.groupby('year_of_release').agg({'name':'count'})
games_sales = games_sales.rename(columns={'name':'Number of games sold'}, level = 0)
games_sales.index = games_sales.index.rename('year')


# In[13]:


games['year_of_release'].fillna(games['year_of_release'].mean(), inplace=True)  # fill NaN with mean
games['year_of_release'] = games['year_of_release'].astype(int)


# In[14]:


games_sales = games.pivot_table(index='year_of_release', values='name', aggfunc='count').reset_index()

sns.set_style('whitegrid')
plt.figure(figsize=(20, 5))
sns.countplot(data = games, x='year_of_release');
plt.title('Total game sales by year')
plt.ylabel('Total sales, millions of copies sold')
plt.xlabel('year')


# 

# Here, we observe a strong left skew in the disttibution of games released with the central point being around 2008/2009. This trend likely has an interesting relationship with model of platform or genre released that will need to be investigated at a different time. What I am getting at is that there were landmark events in this market caused growth like this and are primary related to adoption of new platforms and popular games.

# ### Look at how sales varied from platform to platform. Choose the platforms with the greatest total sales and build a distribution based on data for each year. Find platforms that used to be popular but now have zero sales. How long does it generally take for new platforms to appear and old ones to fade?

# 

# In[15]:


#Form a new dataframe for Total Platform Sales
total_platform_sales = games.groupby('platform')[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum().reset_index()

total_platform_sales['ww_total'] = total_platform_sales[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)


# In[16]:


# Sort the data from highest to lowest
sorted_data = sorted(zip(total_platform_sales['platform'], total_platform_sales['ww_total']), key=lambda x: x[1], reverse=True)

# Create a horizontal bar chart
fig, ax = plt.subplots()
ax.barh([x[0] for x in sorted_data], [x[1] for x in sorted_data])

# Add labels to each bar
for i, v in enumerate(sorted_data):
    ax.text(v[1], i - 0.15, str(v[1]), color='white', fontweight='bold')

# Set the title and labels
ax.set_xlabel('Sales (millions)')
ax.set_ylabel('Platforms')
ax.set_title('Total Sales by Platform (2017)')
ax.set_yticks([x[0] for x in sorted_data])
ax.set_yticklabels([x[0] for x in sorted_data])

# Adjust the size of the figure
fig.set_size_inches(11, 8)

# Display the plot
plt.show()


# In[17]:


# Find platforms that used to be popular but now have zero sales
popular_platforms = games[(games['na_sales'] > 0) | (games['eu_sales'] > 0) | (games['jp_sales'] > 0) | (games['other_sales'] > 0)]['platform'].unique()
zero_sales_platforms = games[(games['na_sales'] == 0) & (games['eu_sales'] == 0) & (games['jp_sales'] == 0) & (games['other_sales'] == 0)]['platform'].unique()
former_popular_platforms = [platform for platform in popular_platforms if platform in zero_sales_platforms]

print(former_popular_platforms)


# In[18]:


# Calculate the total sales for each platform
games['total_sales'] = games[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

display(games.head(5))


# In[19]:


# fill NaN values with 0 (or any other value that makes sense for your data)
games['year_of_release'].fillna(0, inplace=True)
games['total_sales'].fillna(0, inplace=True)

# convert 'year_of_release' and 'total_sales' to int
games['year_of_release'] = games['year_of_release'].astype(int)
games['total_sales'] = games['total_sales'].astype(int)

games = games[games['year_of_release']!= 0]

# group by 'year_of_release' and 'platform', and sum 'total_sales'
grouped_df = games.groupby(['year_of_release', 'platform'])['total_sales'].sum().reset_index()

plt.figure(figsize=(15, 8)) 

# plot 'total_sales' by 'year_of_release' with 'platform' as separate series
for platform in games['platform'].unique():
    platform_df = grouped_df[grouped_df['platform'] == platform]
    plt.plot(platform_df['year_of_release'], platform_df['total_sales'], label=platform)

plt.xlabel('Year of Release')
plt.ylabel('Total Sales')
plt.title('Total Sales by Year of Release and Platform')
plt.legend()
plt.show()


# <div class="alert alert-block alert-success">✔️
# 
# __Reviewer's comment №1__
# 
# 
# PS2 data distribution looks like a cat ^^

# The two platforms that had were market leaders then faded away were the Sony PS2 and PS3 systems – which I remember clearly. Xbox 360 was not flagged in my algorithm likely because its sales did not decline as much. Based on the final multi-series line graph, we see that it takes about 5 to 8 years for the launch life of a platform with steep share growth in the first 3 to 4 years, followed by step declines while it is being phased out.

# ### Determine what period you should take data for. To do so, look at your answers to the previous questions. The data should allow you to build a model for 2017.

# In[20]:


#Use 1995 as the cutoff for year_of_release based on previous histogram in 3.1
games_slice = games[games['year_of_release'] >= 2005]


display(games_slice)


# <div class="alert alert-block alert-danger">✍
# 
# __Reviewer's comment №1__
# 
# 
# For the purpose of predicting sales for the next year, even traditional businesses rarely take data for more than 2-3 years. And in such a dynamically changing industry as computer games, you shouldn't take too long a time interval - otherwise you're bound to capture trends that are already outdated. But you shouldn't take too short a period either

# ### Which platforms are leading in sales? Which ones are growing or shrinking? Select several potentially profitable platforms.

# In[21]:


#Determine year to year slope to see which sales are growing or shrinking.
games_slice.groupby('platform')['total_sales'].sum().nlargest(10)

from scipy.stats import linregress

# Assuming 'games' is your original dataframe
games_by_year = games_slice.groupby(['platform', 'year_of_release'])['total_sales'].sum().unstack().reset_index()
games_by_year.set_index('platform', inplace=True)

games_by_year['slope'] = games_by_year.apply(lambda x: linregress(range(len(x)), x)[0] if len(x) >= 2 else np.nan, axis=1)

display(games_by_year)


# The approach that I took here was a slope based method to detect consecutive years of growth, stability, or decline in sales. From here, you see some growth in the PC market and X360 market despite a general decline in this indstruy. My approach still requires the user to use their eyes to detect the trend and judgement to discern the directionality, but there is evidence that if we are looking at 2014 through 2016, all platform sales are tanking. My suspicion that this is a cyclical attribute of the industry most impacted by the age group who drove peaks over the past two decades and the economic status of younger players.

# ### Build a box plot for the global sales of all games, broken down by platform. Are the differences in sales significant? What about average sales on various platforms? Describe your findings.

# In[22]:


# Fill NaN values in the 'total_sales' column with 0
games['total_sales'].fillna(0, inplace=True)

# Convert the 'total_sales' column to integer
games['total_sales'] = games['total_sales'].astype(int)

# Group the data by platform
grouped_data = games.groupby('platform')

# Create a list of arrays, one for each platform
data_to_plot = [group['total_sales'] for _, group in grouped_data]

# Create a list of labels, one for each platform
labels = [platform for platform, _ in grouped_data]

# Create a box plot of the total sales by platform
plt.figure(figsize=(12,6))
plt.boxplot(data_to_plot, labels=labels)
plt.xlabel('')
plt.ylabel('Global Sales (millions)')
plt.title('Global Sales of Video Games by Platform')

# Set the y-axis limits
plt.ylim(0, 10)

plt.show()


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Unfortunately, this graph only shows the outliers, and does not show the median and 75% quantile. For more reasonable conclusions it is necessary to make an additional graph, where only the lower part of the boxplots will be displayed. This can be achieved, for example, by setting the parameter ylim
# </div>

# <div class="alert alert-block alert-success">✔️
# 
# __Reviewer's comment №2__
#     
# Great

# Differences in sales are very different both demonstrated by the presence and spread of outliers as well as the platforms who did not deviate from the average. This algorithm does not detect a noticeable difference in averages at this point. To be more accurate, perhaps we implement an area-under-the-curve method at a later time. Upon closer inspection by adjusting the y-lim, I see that the weightage from outliers in the cases of PS and XB series must outweigh average too much due to number of games in the denomenator. 

# In[23]:


# Group the data by platform and calculate the total sales for each region
platform_sales = games.groupby('platform')[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum().reset_index()

# Convert the sales columns to integer
platform_sales[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']] = platform_sales[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].astype(int)

# Calculate the total sales for each platform
platform_sales['total_sales'] = platform_sales[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

# Create a stacked bar chart of the sales for each platform broken down by region
plt.figure(figsize=(15,6))
plt.bar(platform_sales['platform'], platform_sales['na_sales'], label='North America', color='red')
plt.bar(platform_sales['platform'], platform_sales['eu_sales'], label='Europe', color='green')
plt.bar(platform_sales['platform'], platform_sales['jp_sales'], label='Japan', color='blue')
plt.bar(platform_sales['platform'], platform_sales['other_sales'], label='Other', color='orange')
plt.xlabel('Platform')
plt.ylabel('Sales (in millions)')
plt.title('Sales of Video Games by Platform and Region')
plt.legend()
plt.show()


# ##### Lovely graph reinforcing the algorithm where we pull out PS2 and PS3 as the leaders who decline more. It clearly shows X360 as being more dominant than PS2, but perhaps held share for long – likely based on experience. We also clearly see Nintendo's Wii and DS in the top sales list.

# ### Take a look at how user and professional reviews affect sales for one popular platform (you choose). Build a scatter plot and calculate the correlation between reviews and sales. Draw conclusions.

# In[24]:


#Isolate data for Xbox 360 per the instructions
x360_games = games[games['platform'] == 'X360']

# Display the resulting dataframe
display(x360_games)


# In[25]:


#Create a two series scatterplot for the relationship between Xbox 360 sales and ratings, then add a slope line and R-squared value
# Create a single dataframe with both critic scores and user scores
x360_games = x360_games.replace('tbd', np.nan).replace([np.inf, -np.inf], np.nan).fillna(0)
scores = x360_games[['critic_score', 'user_score', 'total_sales']].copy()

display(scores.head())


# In[26]:


# Isolate data for Xbox 360 per the instructions
x360_games = games[games['platform'] == 'X360']

# Replace 'tbd' with NaN, and Inf/-Inf with NaN
x360_games = x360_games.replace('tbd', np.nan).replace([np.inf, -np.inf], np.nan)

# Fill NaN values with either NaN or 0
fill_value = np.nan  # or 0, depending on your preference
x360_games.fillna(fill_value, inplace=True)

# Create a single dataframe with both critic scores and user scores
scores = x360_games[['critic_score', 'user_score', 'total_sales']].copy()


# In[27]:


print(scores[['critic_score', 'user_score']].isna().sum())


# In[28]:


print(np.isinf(scores[['critic_score', 'user_score']]).sum())


# In[29]:


# Calculate the minimum and maximum values for the x-axis
critic_min = scores['critic_score'].min()
user_min = scores['user_score'].min()
critic_max = scores['critic_score'].max()
user_max = scores['user_score'].max()

print(critic_min, user_min, critic_max, user_max)


# In[30]:


# Calculate the mean of each column, excluding NaN values
mean_critic_score = scores['critic_score'].dropna().mean()
mean_user_score = scores['user_score'].dropna().mean()
mean_total_sales = scores['total_sales'].dropna().mean()

# Replace NaN with the mean
scores['critic_score'].fillna(mean_critic_score, inplace=True)
scores['user_score'].fillna(mean_user_score, inplace=True)
scores['total_sales'].fillna(mean_total_sales, inplace=True)


# In[31]:


# Divide user_score by e+10 and multiply by 10
scores['user_score'] = scores['user_score'].astype(float)
scores['user_score'] = scores['user_score'] *10


# In[32]:


plt.figure(figsize=(12, 6))

# Create a scatter plot of both critic scores and user scores vs. sales
sns.scatterplot(x='critic_score', y='total_sales', data=scores, color='#406d9c', label='Critic Reviews', alpha=0.5)
sns.scatterplot(x='user_score', y='total_sales', data=scores, color='#cf850c', label='User Reviews', alpha=0.5)

# Add a legend
plt.legend()

# Add axis labels and a title
plt.xlabel('Score')
plt.ylabel('Sales (in millions)')
plt.title('X360 Sales vs. Reviews')

# Set the x-axis limits to the minimum and maximum values in the data
plt.xlim(np.nanmin([scores['critic_score'].min(), scores['user_score'].min()]),
         np.nanmax([scores['critic_score'].max(), scores['user_score'].max()]))

# Calculate the slope and r-squared for critic scores
critic_regression = linregress(scores['critic_score'], scores['total_sales'])
critic_slope = critic_regression.slope
critic_r_squared = critic_regression.rvalue ** 2

# Calculate the slope and r-squared for user scores
user_regression = linregress(scores['user_score'], scores['total_sales'])
user_slope = user_regression.slope
user_r_squared = user_regression.rvalue ** 2

# Add slope lines and r-squared values
plt.plot(scores['critic_score'], critic_slope * scores['critic_score'] + critic_regression.intercept, color='#406d9c', linestyle='--', label=f'Critic Reviews Slope: {critic_slope:.2f}, R²: {critic_r_squared:.2f}')
plt.plot(scores['user_score'], user_slope * scores['user_score'] + user_regression.intercept, color='#cf850c', linestyle='--', label=f'User Reviews Slope: {user_slope:.2f}, R²: {user_r_squared:.2f}')

# Show the plot
plt.show()


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
# 
# Error code ![image.png](attachment:image.png)
#     
# Please fix it

# In[33]:


print('The r-squared value for User Reviews to Sales is : ', round(user_r_squared,2))
print('The r-squared value for Critic Reviews to Sales is : ', round(critic_r_squared,2))


# In[34]:


#Create correlation matrix for sales to scores
# Select the columns of interest
cols = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'total_sales', 'user_score', 'critic_score']

# Create a new DataFrame with the selected columns
df = games[cols].copy()

# Drop rows with NaN values
df = df.dropna()

# Replace 'tbd' with 0
df = df.replace('tbd', 0)

# Convert the columns to float
df = df.astype(float)

# Create a correlation matrix
corr_matrix = df.corr()

# Create a heatmap using seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()


# Here, scores were normalized to be multiplied by 10 for pre-processing reasons. I applied a linear fit to determine initial relatedness and it finds that there is no relationship between X360 sales and user or critic ratings of games. Very important to note that the ratings are of games and not of the hardware. Next, my favorite analysis and what I am using in my own app that I am seeking investors for. The correl tells us that the only dependancies are between regional and total sales. there is a moderate (low in my opinion) relationship between user and critic score of which the latter are likely influenced greatly by the former due to consumer psychology in the demographic of game users.

# ### Keeping your conclusions in mind, compare the sales of the same games on other platforms.

# In[35]:


#Create a pivot tabel to compare sales of the same games on different platforms
# Group the data by game name and platform, and sum the total sales
grouped_df = games.groupby(['name', 'platform'])['total_sales'].sum().reset_index()

# Pivot the data to create separate columns for each platform
pivot_df = grouped_df.pivot(index='name', columns='platform', values='total_sales')

# Display the pivot table
display(pivot_df)


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
#     
#     
# The assignment is to relate the conclusions to the sales of games on other platforms, because the conclusions based on calculations across multiple platforms look "weightier" and more convincing
# </div>

# In[36]:


# Sort the DataFrame by the 'ww_total' column in descending order
sorted_data = total_games_sales.sort_values(by='ww_total', ascending=False)

# Display the head and tail of the sorted DataFrame
print("Top 20 games by worldwide sales (in millions):")
display(sorted_data.head(20))
print("\nBottom 5 games by worldwide sales (in millions):")
display(sorted_data.tail())


# In response to the feedback, I have decided to look at games sales as a cumulative value across years and platforms to determine which were the highest selling. There is no easy way to make a comparison given the volumne of games released even in the slices. Some insights are of course the top five games and familiar names, but more importantly, there is a distinct trend between the first five games in the form of a revenue difference. I expect this to take place a few times lower on the list because there are many niches in this industry which result in sales that are relatively low.

# ### Take a look at the general distribution of games by genre. What can we say about the most profitable genres? Can you generalize about genres with high and low sales?

# In[37]:


#Get count of games per year and plot
genre_counts = games['genre'].value_counts()

# Create a bar chart
plt.figure(figsize=(12, 6))
genre_counts.plot(kind='bar')
plt.title('Distribution of Games by Genre (1980 – 2016)')
plt.xlabel('Genre')
plt.ylabel('Number of Games')
plt.xticks(rotation=0)

# Add data labels to the bars
for i, v in enumerate(genre_counts):
    plt.text(i, v + 0.5, str(v), ha='center')

plt.show()


# In[38]:


#Calculate sum of sales by genre
# Group by genre and calculate sum of total sales
genre_sales = games.groupby('genre')['total_sales'].sum().reset_index()

# Sort by total sales in descending order
genre_sales = genre_sales.sort_values('total_sales', ascending=False)

display(genre_sales)


# In[39]:


#Plot sales by genre and year
# Pivot the data to get total sales by genre and year
genre_year_sales = games.pivot_table(index=['genre', 'year_of_release'], values='total_sales', aggfunc='sum').reset_index()

# Sort by total sales in descending order
genre_year_sales = genre_year_sales.sort_values('total_sales', ascending=False)

# Get the top 10 most profitable genres
top_genres = genre_year_sales.groupby('genre')['total_sales'].sum().reset_index().sort_values('total_sales', ascending=False).head(10)

# Create a figure with a specified width
plt.figure(figsize=(12, 6))  # adjust the width and height as needed

# Plot the top 10 genres over time
sns.lineplot(x='year_of_release', y='total_sales', hue='genre', data=genre_year_sales[genre_year_sales['genre'].isin(top_genres['genre'])])

plt.title('Top 10 Most Profitable Genres Over Time')
plt.xlabel('Year')
plt.ylabel('Total Sales (in millions)')
plt.legend(title='Genre')

plt.show()


# In[40]:


# Set the figure size
plt.figure(figsize=(12, 6))

# Group the data by genre and calculate the sum of total_sales for each genre
total_sales_by_genre = games.groupby('genre')['total_sales'].mean().reset_index()

sales_by_genre = total_sales_by_genre.sort_values(by='total_sales', ascending=False)

# Create a bar chart for each genre (boxplot might not be suitable for total sales)
sns.barplot(x='genre', y='total_sales', data=sales_by_genre)  # Change boxplot to barplot

# Update labels and title
plt.xlabel('Genre')
plt.ylabel('Average Total Sales (in millions)')  # Update y-axis label
plt.title('Average Total Sales by Genre')

# Show the plot
plt.show()


# This research shows a lot of volatility in this market that is most demonstrated by the competitive dynamics within a genre of games. I deduce this because of the greater volatility over time compared to what we sale in the platform sales portion of this analysis. Now, the bar chart is a clearer insight than the multi-series line chart, but nonetheless time series are more profound. So, we notice peak trends in genre which likely correspond to specific game releases (i.e., FIFA or 2K in Sports, Call of Duty in Shooter, Others in Action). The second bar plot shows a different perspective where we look at profitability from the perspective of average sales. This normalizes the results based on how many games are in that genre. Boxplot is not possible because the datest does not allow for a series of averages and the ['total_sales'] data itself is too skewed by outliers with the 50th percintile being shown above.

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Your calculations need to be supplemented a little more. Total sales is a poor metric for finding the most profitable genre. High overall sales numbers can hide a lot of small games with low sales. Or 2-3 stars and a bunch of failures. It's better to find a genre where games consistently bring in high revenue - for that it's worth considering average or median sales
#     
# ---
#     
# Ideally, visualize the data distribution using boxplot()
# </div>

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №2__
# 
# I agree

# ## Step 4: Create a User Profile for Each Region

# ### For each region (NA, EU, JP), determine the top five platforms. Describe variations in their market shares from region to region.
# 

# In[41]:


print("Original games shape:", games.shape)


# In[42]:


# assume 'games' is a Pandas DataFrame with columns 'na_sales', 'eu_sales', 'jp_sales', 'other_sales'

# create separate DataFrames for each region
north_america_games = games[games['na_sales'] > 0].copy()
europe_games = games[games['eu_sales'] > 0].copy()
jp_games = games[games['jp_sales'] > 0].copy()
other_games = games[games['other_sales'] > 0].copy()


# assume north_america_games, europe_games, jp_games, other_games are DataFrames

regions = {
    'north_america': {'df': north_america_games, 'sales_col': 'na_sales'},
    'europe': {'df': europe_games, 'sales_col': 'eu_sales'},
    'jp': {'df': jp_games, 'sales_col': 'jp_sales'},
    'other': {'df': other_games, 'sales_col': 'other_sales'}
}

region_selector = 'north_america'

region_df = regions[region_selector]['df']
sales_col = regions[region_selector]['sales_col']

sales_cols = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales']
sales_col_selector = "na_sales"

def top_platforms_by_sales(df, sales_col):
    return df.groupby('platform')[sales_col].sum().sort_values(ascending=False).head(5)

top_platforms_by_sales_df = top_platforms_by_sales(region_df, sales_col)
print(f"Top 5 platforms by games sales in {region_selector}:")
print(top_platforms_by_sales_df)

def top_platforms_by_games(df):
    return df['platform'].value_counts().head(5)

top_platforms_by_games_df = top_platforms_by_games(region_df)
print(f"Top 5 platforms by number of games in {region_selector}:")
print(top_platforms_by_games_df)

def top_genres_by_region(df):
    return df['genre'].value_counts().head(5)

top_genres_by_region_df = top_genres_by_region(region_df)
print(f"Top 5 genres in {region_selector}:")
print(top_genres_by_region_df)

def analyze_esrb_ratings(df, sales_col):
    esrb_ratings = df.groupby('rating')[sales_col].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(esrb_ratings['rating'], esrb_ratings[sales_col])
    ax.set_xlabel('ESRB Rating')
    ax.set_ylabel('Cumulative Sales')
    ax.set_title('ESRB Ratings vs. Cumulative Sales')
    return fig


# In[43]:


# assume 'games' is a Pandas DataFrame with columns 'na_sales', 'eu_sales', 'jp_sales', 'other_sales'

# create separate DataFrames for each region
north_america_games = games[games['na_sales'] > 0].copy()
europe_games = games[games['eu_sales'] > 0].copy()
jp_games = games[games['jp_sales'] > 0].copy()
other_games = games[games['other_sales'] > 0].copy()


# assume north_america_games, europe_games, jp_games, other_games are DataFrames

regions = {
    'north_america': {'df': north_america_games, 'sales_col': 'na_sales'},
    'europe': {'df': europe_games, 'sales_col': 'eu_sales'},
    'jp': {'df': jp_games, 'sales_col': 'jp_sales'},
    'other': {'df': other_games, 'sales_col': 'other_sales'}
}

region_selector = 'europe'

region_df = regions[region_selector]['df']
sales_col = regions[region_selector]['sales_col']

sales_cols = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales']
sales_col_selector = "na_sales"

def top_platforms_by_sales(df, sales_col):
    return df.groupby('platform')[sales_col].sum().sort_values(ascending=False).head(5)

top_platforms_by_sales_df = top_platforms_by_sales(region_df, sales_col)
print(f"Top 5 platforms by games sales in {region_selector}:")
print(top_platforms_by_sales_df)

def top_platforms_by_games(df):
    return df['platform'].value_counts().head(5)

top_platforms_by_games_df = top_platforms_by_games(region_df)
print(f"Top 5 platforms by number of games in {region_selector}:")
print(top_platforms_by_games_df)

def top_genres_by_region(df):
    return df['genre'].value_counts().head(5)

top_genres_by_region_df = top_genres_by_region(region_df)
print(f"Top 5 genres in {region_selector}:")
print(top_genres_by_region_df)

def analyze_esrb_ratings(df, sales_col):
    esrb_ratings = df.groupby('rating')[sales_col].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(esrb_ratings['rating'], esrb_ratings[sales_col])
    ax.set_xlabel('ESRB Rating')
    ax.set_ylabel('Cumulative Sales')
    ax.set_title('ESRB Ratings vs. Cumulative Sales')
    return fig


# In[44]:


# assume 'games' is a Pandas DataFrame with columns 'na_sales', 'eu_sales', 'jp_sales', 'other_sales'

# create separate DataFrames for each region
north_america_games = games[games['na_sales'] > 0].copy()
europe_games = games[games['eu_sales'] > 0].copy()
jp_games = games[games['jp_sales'] > 0].copy()
other_games = games[games['other_sales'] > 0].copy()


# assume north_america_games, europe_games, jp_games, other_games are DataFrames

regions = {
    'north_america': {'df': north_america_games, 'sales_col': 'na_sales'},
    'europe': {'df': europe_games, 'sales_col': 'eu_sales'},
    'jp': {'df': jp_games, 'sales_col': 'jp_sales'},
    'other': {'df': other_games, 'sales_col': 'other_sales'}
}

region_selector = 'jp'

region_df = regions[region_selector]['df']
sales_col = regions[region_selector]['sales_col']

sales_cols = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales']
sales_col_selector = "na_sales"

def top_platforms_by_sales(df, sales_col):
    return df.groupby('platform')[sales_col].sum().sort_values(ascending=False).head(5)

top_platforms_by_sales_df = top_platforms_by_sales(region_df, sales_col)
print(f"Top 5 platforms by games sales in {region_selector}:")
print(top_platforms_by_sales_df)

def top_platforms_by_games(df):
    return df['platform'].value_counts().head(5)

top_platforms_by_games_df = top_platforms_by_games(region_df)
print(f"Top 5 platforms by number of games in {region_selector}:")
print(top_platforms_by_games_df)

def top_genres_by_region(df):
    return df['genre'].value_counts().head(5)

top_genres_by_region_df = top_genres_by_region(region_df)
print(f"Top 5 genres in {region_selector}:")
print(top_genres_by_region_df)

def analyze_esrb_ratings(df, sales_col):
    esrb_ratings = df.groupby('rating')[sales_col].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(esrb_ratings['rating'], esrb_ratings[sales_col])
    ax.set_xlabel('ESRB Rating')
    ax.set_ylabel('Cumulative Sales')
    ax.set_title('ESRB Ratings vs. Cumulative Sales')
    return fig


# In[45]:


# assume 'games' is a Pandas DataFrame with columns 'na_sales', 'eu_sales', 'jp_sales', 'other_sales'

# create separate DataFrames for each region
north_america_games = games[games['na_sales'] > 0].copy()
europe_games = games[games['eu_sales'] > 0].copy()
jp_games = games[games['jp_sales'] > 0].copy()
other_games = games[games['other_sales'] > 0].copy()


# assume north_america_games, europe_games, jp_games, other_games are DataFrames

regions = {
    'north_america': {'df': north_america_games, 'sales_col': 'na_sales'},
    'europe': {'df': europe_games, 'sales_col': 'eu_sales'},
    'jp': {'df': jp_games, 'sales_col': 'jp_sales'},
    'other': {'df': other_games, 'sales_col': 'other_sales'}
}

region_selector = 'other'

region_df = regions[region_selector]['df']
sales_col = regions[region_selector]['sales_col']

sales_cols = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales']
sales_col_selector = "na_sales"

def top_platforms_by_sales(df, sales_col):
    return df.groupby('platform')[sales_col].sum().sort_values(ascending=False).head(5)

top_platforms_by_sales_df = top_platforms_by_sales(region_df, sales_col)
print(f"Top 5 platforms by games sales in {region_selector}:")
print(top_platforms_by_sales_df)

def top_platforms_by_games(df):
    return df['platform'].value_counts().head(5)

top_platforms_by_games_df = top_platforms_by_games(region_df)
print(f"Top 5 platforms by number of games in {region_selector}:")
print(top_platforms_by_games_df)

def top_genres_by_region(df):
    return df['genre'].value_counts().head(5)

top_genres_by_region_df = top_genres_by_region(region_df)
print(f"Top 5 genres in {region_selector}:")
print(top_genres_by_region_df)

def analyze_esrb_ratings(df, sales_col):
    esrb_ratings = df.groupby('rating')[sales_col].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(esrb_ratings['rating'], esrb_ratings[sales_col])
    ax.set_xlabel('ESRB Rating')
    ax.set_ylabel('Cumulative Sales')
    ax.set_title('ESRB Ratings vs. Cumulative Sales')
    return fig


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Error code ![image.png](attachment:image.png)

# ## Step 5: Test the following hypotheses

# #### Average user ratings of the Xbox One and PC platforms are the same

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №2__
# 
# Correct interpretation of the Null and Alternative hypotheses

# In[46]:


#Null: Average user ratings of the Xbox One and PC platforms are the same

#Alternative: Average user ratings of the Xbox One and PC platforms are not the same

#Test: One-sample, two-sided t-test

def t_test_and_p_value(data1, data2):
    t_statistic, p_value = stats.ttest_ind(data1, data2)
    return t_statistic, p_value

def hypothesis_test_1():
    xbox_ratings = games[games["platform"] == "XOne"]["user_score"]
    pc_ratings = games[games["platform"] == "PC"]["user_score"]

    t_statistic, p_value = t_test_and_p_value(xbox_ratings, pc_ratings)

    print("Hypothesis Test 1: Xbox One vs PC")
    print("**Null Hypothesis:** Average user ratings for Xbox One and PC platforms are the same.")
    print("**Alternative Hypothesis:** Average user ratings for Xbox One and PC platforms are different.")
    print(f"**T-statistic:** {t_statistic:.2f}")
    print(f"**P-value:** {p_value:.3f}")

    if p_value < 0.05:
        print("**Conclusion:** Reject the null hypothesis. There is statistically significant evidence to suggest that average user ratings for Xbox One and PC platforms are different.")
    else:
        print("**Conclusion:** Fail to reject the null hypothesis. There is not enough evidence to suggest that average user ratings for Xbox One and PC platforms are different.")


# #### Average user ratings for the Action and Sports genres are different

# In[47]:


def hypothesis_test_2():
    action_ratings = games[games["genre"] == "Action"]["user_score"].replace(0, np.nan).fillna(games[games["genre"] == "Action"]["user_score"].mean())
    sports_ratings = games[games["genre"] == "Sports"]["user_score"].replace(0, np.nan).fillna(games[games["genre"] == "Sports"]["user_score"].mean())

    # Check if there are enough ratings for both genres
    if len(action_ratings) < 2 or len(sports_ratings) < 2:
        print("Not enough ratings for one or both genres. Cannot perform t-test.")
        return

    # Calculate the mean of the Action genre ratings
    action_mean = action_ratings.mean()
    sports_mean = sports_ratings.mean()

    # Perform one-sample, two-sided t-test
    t_statistic, p_value = stats.ttest_1samp(sports_ratings, action_mean)

    print("Hypothesis Test 2: Action vs Sports")
    print("**Null Hypothesis:** Average user ratings for Action and Sports genres are the same.")
    print("**Alternative Hypothesis:** Average user ratings for Action and Sports genres are different.")
    print(f"**T-statistic:** {t_statistic:.2f}")
    print(f"**P-value:** {p_value:.3f}")

    if p_value < 0.05:
        print("**Conclusion:** Reject the null hypothesis. There is statistically significant evidence to suggest that average user ratings for Action and Sports genres are different.")
    else:
        print("**Conclusion:** Fail to reject the null hypothesis. There is not enough evidence to suggest that average user ratings for Action and Sports genres are different.")


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №2__
# 
# 
# When conducting hypothesis tests, it's crucial to test the hypotheses based on the characteristics of the data rather than pre-aggregated values. Grouping data before hypothesis testing can lead to a biased interpretation of the results. Hypothesis tests are designed to evaluate specific characteristics or relationships within the data, and grouping can introduce additional dependencies or overlook important nuances in the data.
# 
# For accurate and reliable hypothesis testing, it's recommended to work with the raw data without pre-grouping or aggregation. By directly testing the hypotheses based on the individual data points, you ensure a more robust analysis and valid conclusions that reflect the true nature of the dataset.
# 
# Therefore, for hypothesis testing, it's best to work with the original dataset without unnecessary data manipulation that may alter the outcomes of the statistical tests.
# 

# In[48]:


hypothesis_test_1()
hypothesis_test_2()


# ## Step 6: Write a general conclusion

# A general conclusion is that the distribution of platform sales across regions is directionally the same with few noticeable exceptions (i.e., Nintendo DS has higher share in JP vs. other markets). We conclude that Action, Sports, and Shooter are the categories with the most interest from customer, while platformer and shooter have the highest average sales per game release which is valuable to new product planning. Ratings have no effect on Xbox360 sales an insight that likely carries to the other platforms. Without focusing on descriptive statistics, I would like to lastly add that the market is highly competitive amongst leading platforms and specific game genres. We did not explore specific games, but I assume we would see the intra-genre competition clearly. Visit these two links for additional information: https://drive.google.com/file/d/1T2WyOqvxl1ohokqSDuvyuOYA9xRbORwa/view?usp=sharing and https://tripleten5.onrender.com/.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №2__
# 
# 
# Otherwise it's great😊. =)   
#     
# Congratulations on the successful completion of the project 😊👍
# And I wish you success in new works 😊
