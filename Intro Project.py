#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid green 2px; padding: 20px">
#     
# <div class="alert alert-success">
# <b>Review summary, v.5</b> 
#     
# Hello Nicholas. Thanks for you being so dedicated to fixing the code. You did a very good job on imrpoving the project and it worked almost from the beginning to the end.
#     
#     
# <div class="alert alert-warning">
#     
# 
#     
# The last step did not match the instructions, so I showed the code how you need to solve it.
# 
# </div>
#     
# The project is approved.
#     
# Thanks again for your efforts and keep up the good work.

# <div style="border:solid green 2px; padding: 20px">
#     
# <div class="alert alert-success">
# <b>Review summary, v.4</b> 
#     
# Hello Nicholas.
#     
# Thank you for keeping trying to fix the code. You did some good updates. 
#     
#     
# <div class="alert alert-danger">
# 
# There were a few moments which I had to fix, I left comment about that. 
#     
# There are still two last steps that require updates. I tried to add detailed comments on what needs to be fixed.  
# 
# Could you please try to update them?
#     
# If you need help, you can ask for a 1-1 session with a tutor / attend a coworking session.
# 
# 
# </div>
#     
#     
# I'll be looking forward to getting your updated project.

# <div style="border:solid green 2px; padding: 20px">
#     
# <div class="alert alert-success">
# <b>Review summary, v.3</b> 
#     
# Hello Nicholas.
#     
# Thanks for the updates.
#     
#     
# <div class="alert alert-danger">
# 
# I tried to give more detailed instructions and fixed the code in some cases. Please read my instruction and try to follow them to get the required results. 
#     
# If you need help, you can ask for a 1-1 session with a tutor / attend a coworking session.
# 
# 
# </div>
#     
#     
# I'll be looking forward to getting your updated project.

# <div style="border:solid green 2px; padding: 20px">
#     
# <div class="alert alert-success">
# <b>Review summary, v.2</b> 
#     
# Hello Nicholas.
#     
# Thanks for the updates.
#     
#     
# <div class="alert alert-danger">
# 
# The project is still not complete and has code errors. Could you please complete the project, make sure there are no code errors and then submit it for review. 
#     
# If you have difficulties with that, you need to contact your Community Manager and ask for a 1-1 session with a tutor / attend a coworking session.
# 
# 
# </div>
#     
#     
# I'll be looking forward to getting your updated notebook.

# <div style="border:solid blue 2px; padding: 20px">
#   
# **Hello Nicholas.**
# 
# My name is Yulia, and I will be reviewing your project. 
# 
# You will find my comments in coloured cells marked as 'Reviewer's comment'. The cell colour will vary based on the contents - I am explaining it further below. 
# 
# **Note:** Please do not remove or change my comments - they will help me in my future reviews and will make the process smoother for both of us. 
# 
# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment</b> 
#     
# Such comment will mark efficient solutions and good ideas that can be used in other projects.
# </div>
# 
# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment</b> 
#     
# The parts marked with yellow comments indicate that there is room for optimisation. Though the correction is not necessary it is good if you implement it.
# </div>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment</b> 
#     
# If you see such a comment, it means that there is a problem that needs to be fixed. Please note that I won't be able to accept your project until the issue is resolved.
# </div>
# 
# You are also very welcome to leave your comments / describe the corrections you've done / ask me questions, marking them with a different colour. You can use the example below: 
# 
# <div class="alert alert-info"; style="border-left: 7px solid blue">
# <b>Student's comment</b>

# <div style="border:solid green 2px; padding: 20px">
#     
# <div class="alert alert-success">
# <b>Review summary</b> 
#     
# Nicholas, thanks for submitting the project. You made a good start.
#     
# - I can see that you already know many python methods that allow to thoroughly study dataframes 
# - You know how to find and remove missing values and duplicates
# - You can write your own functions, can use conditional indexing and many other python methods
#     
# <div class="alert alert-danger">
# 
# However, there are some critical comments that need to be corrected. You will find them in the red-coloured cells in relevant sections.
#     
# Could you please fix them and send the project back to me?
#     
# Please also note that you need to complete the project before submitting it for review. If you have difficulties, please do not hesitate to contact your Community Manager and ask for a 1-1 session with a tutor.
# 
# 
# </div>
#     
# You may also work on the yellow comments. If you have any questions please write them when you return your project. 
#     
# I'll be looking forward to getting your updated notebook.

# ## Basic Python - Project <a id='intro'></a>

# ## Introduction <a id='intro'></a>
# In this project, you will work with data from the entertainment industry. You will study a dataset with records on movies and shows. The research will focus on the "Golden Age" of television, which began in 1999 with the release of *The Sopranos* and is still ongoing.
# 
# The aim of this project is to investigate how the number of votes a title receives impacts its ratings. The assumption is that highly-rated shows (we will focus on TV shows, ignoring movies) released during the "Golden Age" of television also have the most votes.
# 
# ### Stages 
# Data on movies and shows is stored in the `/datasets/movies_and_shows.csv` file. There is no information about the quality of the data, so you will need to explore it before doing the analysis.
# 
# First, you'll evaluate the quality of the data and see whether its issues are significant. Then, during data preprocessing, you will try to account for the most critical problems.
#  
# Your project will consist of three stages:
#  1. Data overview
#  2. Data preprocessing
#  3. Data analysis

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# Title and introduction are essential parts of the project. Make sure you do not forget to include it in your further projects. 
#     
# It is optimal if introduction consists of:
#     
# - brief description of the situation;
# - goal of the project;
# - description of the data we are going to use.
# </div>
# 

# ## Stage 1. Data overview <a id='data_review'></a>
# 
# Open and explore the data.

# You'll need `pandas`, so import it.

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# ✔️ 
#     
# <strike>
# 
# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 1</b> 
# 
# I noticed that the cell count starts not from 1. It is highly recommended to restart the kernel and run all the sells before submitting the project. 
#     
# To do so, go to the menu and do `Kernel -> Restart and Run All`. 
#     
# Restarting the kernel is important to make sure that all variables and methods stored in the memory have been removed. This way you can be sure that you see the same result the reviewer will get.

# In[1]:


# importing pandas
import pandas as pd


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# 
# It's a good practice to upload all necessary libraries in the first code cell, separately from datasets (so that you do not have to reload the dataset if you need to add another library). 

# Read the `movies_and_shows.csv` file from the `datasets` folder and save it in the `df` variable:

# In[2]:


# reading the files and storing them to df
df = pd.read_csv('/datasets/movies_and_shows.csv')


# Print the first 10 table rows:

# In[3]:


# obtaining the first 10 rows from the df table
# hint: you can use head() and tail() in Jupyter Notebook without wrapping them into print()
print(df.head(10))


# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 1</b> 
# 
# The `print()` function is not good for displaying dataframes in Jupyter notebook. 
#     
# Sometimes you don't need any function to display a dataframe, for example, if you are calling it in the last line of a code cell.
#     
# In other cases it is preferrable to use `display()` instead of `print()`. Then dataframe will be shown in a table format, which is much easier to read.

# Obtain the general information about the table with one command:

# In[4]:


# obtaining general information about the data in df
df.info()


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# Great - you've used a comprehensive set of methods to have a first look at the data.

# The table contains nine columns. The majority store the same data type: object. The only exceptions are `'release Year'` (int64 type), `'imdb sc0re'` (float64 type) and `'imdb v0tes'` (float64 type). Scores and votes will be used in our analysis, so it's important to verify that they are present in the dataframe in the appropriate numeric format. Three columns (`'TITLE'`, `'imdb sc0re'` and `'imdb v0tes'`) have missing values.
# 
# According to the documentation:
# - `'name'` — actor/director's name and last name
# - `'Character'` — character played (for actors)
# - `'r0le '` — the person's contribution to the title (it can be in the capacity of either actor or director)
# - `'TITLE '` — title of the movie (show)
# - `'  Type'` — show or movie
# - `'release Year'` — year when movie (show) was released
# - `'genres'` — list of genres under which the movie (show) falls
# - `'imdb sc0re'` — score on IMDb
# - `'imdb v0tes'` — votes on IMDb
# 
# We can see three issues with the column names:
# 1. Some names are uppercase, while others are lowercase.
# 2. There are names containing whitespace.
# 3. A few column names have digit '0' instead of letter 'o'. 
# 

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# 
# 
# Please note that in the next python projects you need to comment your actions, write your observations and insights. 
#     
# You need to use Markdown type of cells for that. To change the cell type for Markdown please use the upper navigation bar - create a new cell with `+` button, step on it and change Raw to Markdown in the dropdown menu.

# ### Conclusions <a id='data_review_conclusions'></a> 
# 
# Each row in the table stores data about a movie or show. The columns can be divided into two categories: the first is about the roles held by different people who worked on the movie or show (role, name of the actor or director, and character if the row is about an actor); the second category is information about the movie or show itself (title, release year, genre, imdb figures).
# 
# It's clear that there is sufficient data to do the analysis and evaluate our assumption. However, to move forward, we need to preprocess the data.

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# Please note that it is highly recommended to add a conclusion / summary after each section and describe briefly your observations and / or major outcomes of the analysis.

# ## Stage 2. Data preprocessing <a id='data_preprocessing'></a>
# Correct the formatting in the column headers and deal with the missing values. Then, check whether there are duplicates in the data.

# In[5]:


# the list of column names in the df table
column_names = df.columns.tolist()
display(column_names)


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# ✔️ Well done.
#     
# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# Could you please display the names of the columns?

# Change the column names according to the rules of good style:
# * If the name has several words, use snake_case
# * All characters must be lowercase
# * Remove whitespace
# * Replace zero with letter 'o'

# In[6]:


# rename columns according to good style
df.columns = [col.lower().strip().replace(' ', '_').replace('0', 'o') for col in df.columns]

print(df.columns)


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 3</b> 
#     
# ✔️ 
#     
# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
#     
# Please add `strip()` to remove the preceding spaces:
#     
# `df.columns = [col.lower().strip().replace(' ', '_').replace('0', 'o') for col in df.columns]`
# 
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# You need first to remove the preceding spaces in `name` and `type` (which are now replaced with underscores). It can be done with `strip()` method. Could you please try to do that?

# Check the result. Print the names of the columns once more:

# In[7]:


# checking result: the list of column names
print(df.columns)


# ### Missing values <a id='missing_values'></a>
# First, find the number of missing values in the table. To do so, combine two `pandas` methods:

# In[8]:


# calculating missing values
num_missing = df.isna().sum()
print(num_missing)


# 
#     
# <strike>
# 
# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 1</b> 
# 
# To see the number of missing values per column, you need to use one `sum()` method (please see below).

# In[9]:


# Added by reviewer
df.isna().sum()


# Not all missing values affect the research: the single missing value in `'title'` is not critical. The missing values in columns `'imdb_score'` and `'imdb_votes'` represent around 6% of all records (4,609 and 4,726, respectively, of the total 85,579). This could potentially affect our research. To avoid this issue, we will drop rows with missing values in the `'imdb_score'` and `'imdb_votes'` columns.

# In[10]:


df_clean = df.dropna(subset=['imdb_score', 'imdb_votes'])

print(df_clean.shape)  # print the new shape of the dataframe


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# ✔️ OK, if you continue working with `df_clean`, it's OK to save the result to it.
#     
# <strike>
# 
# 
# 
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# Please save the result back to `df` variable. As you continue working with it later, and you need to have a dataframe cleaned from the missing values.

# Make sure the table doesn't contain any more missing values. Count the missing values again.

# In[11]:


# counting missing values
num_missing = df_clean.isna().sum()
print(num_missing)


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# ✔️ 
#     
# <strike>
# 
# 
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# Please check the number of missing values in `df` dataframe.

# ### Duplicates <a id='duplicates'></a>
# Find the number of duplicate rows in the table using one command:

# In[12]:


# counting duplicate rows
num_duplicates = df_clean.duplicated().sum()
print('Number of duplicate rows:', num_duplicates)


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 3</b> 
#     
# ✔️ 
#     
# <strike>
# 
# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 1</b> 
# 
# It is more common to use `df.duplicated().sum()` to get the number of the duplicates.

# Review the duplicate rows to determine if removing them would distort our dataset.

# In[13]:


# Produce table with duplicates (with original rows included) and review last 5 rows
duplicates = df[df.duplicated(keep=False)]
print(duplicates.tail(5))


# In[14]:


# ADDED BY REVIEWER
duplicates.sort_values(by='name').tail(5)


# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 4</b> 
# 
# It would also be good to sort the data, so that we can see the duplicates. Please see above how to do that.
#     
# 
#     
# <strike>
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 3</b> 
#     
# You are displaying the last 5 rows of the whole dataframe. And you need to display the last 5 rows of a dataframe that consists of only duplicates. You may create it the following way:
#     
# `duplicates = df[df.duplicated(keep=False)]`
#     
#     
# Could you please create the dataframe, sort it by any column and display the last 5 rows of it?
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
#     
# You need to create a dataframe with the duplicates and display 5 last rows of that dataframe.
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# Could you please display the last five rows of the dataframe with the duplicates?

# There are two clear duplicates in the printed rows. We can safely remove them.
# Call the `pandas` method for getting rid of duplicate rows:

# In[15]:


# removing duplicate rows
num_duplicates = df.drop_duplicates()


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# ✔️ 
#     
# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# Please remove the duplicates from `df` dataframe and confirm below that there are no duplicates left in `df` dataframe.

# Check for duplicate rows once more to make sure you have removed all of them:

# In[16]:


# checking for duplicates
num_duplicates = num_duplicates.duplicated().sum()
print('Number of duplicates:', num_duplicates)


# Now get rid of implicit duplicates in the `'type'` column. For example, the string `'SHOW'` can be written in different ways. These kinds of errors will also affect the result.

# Print a list of unique `'type'` names, sorted in alphabetical order. To do so:
# * Retrieve the intended dataframe column 
# * Apply a sorting method to it
# * For the sorted column, call the method that will return all unique column values

# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 4</b> 
# 
# 
# Here again you continue working with `df` dataframe, while above you saved the result after cleaning the dataframe from missing values and duplicates into a different dataframe. So, I'm adding a block below to clean `df` dataframe from the missing values and duplicates.
# 
#     
# <strike>
# 

# In[17]:


#ADDED BY REVIEWER

df = df.dropna()
df = df.drop_duplicates()


# In[18]:


# AMENDED BY REVIEWER

# Retrieve the intended dataframe column
type_column = df['type'].drop_duplicates()

# Sort the 'type' column
type_column = type_column.sort_values()

# Get the unique values of the 'type' column
unique_types = type_column.unique()

# Print the unique 'type' names
print(unique_types)


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 4</b> 
#     
# ✔️ 
#     
# <strike>
# 
# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 3</b> 
# 
# 
# Please note that I commented out the second line of the code above. This is important, because you need to know what are the current values in the column (what case they have is also important), so that you can make the list of the implicit duplicates later.   
# 
#     
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
# 
# 
# Please note that you don't need to change the case of the types. You need to know the real case of the words to make the list of wrong types. Please display the unique types in the column as they are. It can be done as simply as:
#     
# `df_clean['type'].unique()`
#     
# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# Please show the unique values of `df['type']` column, not the newly created `df_clean` dataframe. 

# Look through the list to find implicit duplicates of `'show'` (`'movie'` duplicates will be ignored since the assumption is about shows). These could be names written incorrectly or alternative names of the same genre.
# 
# You will see the following implicit duplicates:
# * `'shows'`
# * `'SHOW'`
# * `'tv show'`
# * `'tv shows'`
# * `'tv series'`
# * `'tv'`
# 
# To get rid of them, declare the function `replace_wrong_show()` with two parameters: 
# * `wrong_shows_list=` — the list of duplicates
# * `correct_show=` — the string with the correct value
# 
# The function should correct the names in the `'type'` column from the `df` table (i.e., replace each value from the `wrong_shows_list` list with the value in `correct_show`).

# In[19]:


# function for replacing implicit duplicates
def replace_wrong_show(num_duplicates, wrong_shows_list, correct_show):
    # Replace implicit duplicates in the 'type' column
    df['type'] = df['type'].replace(wrong_shows_list, correct_show)
    
wrong_shows_list = ['shows', 'SHOW', 'tv show', 'tv shows', 'tv series', 'tv']
#correct_show = 'show'

# Print the modified DataFrame
print(num_duplicates)


# Call `replace_wrong_show()` and pass it arguments so that it clears implicit duplicates and replaces them with `SHOW`:

# In[20]:


correct_show = 'SHOW'

# Call the function
replace_wrong_show(num_duplicates, wrong_shows_list, correct_show)

# Print the modified DataFrame
print(num_duplicates)


# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 4</b> 
# 
# Well done, you called the function correctly. 
#     
# Please note that I commented out a line in the code block 18, because it's not needed there, you set the value for `correct_show` in the next block.
#     
# 
#     
# <strike>
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 3</b> 
#     
# Please keep only one of the above blocks. It's important to choose the correct one. Because if you keep the upper block, you'll replace the implicit duplicates with `'show'`, and if you choose the lower one - you'll replace the duplicates with `'SHOW'`.
#     
# ---
#     
# And a very important thing - you need to call the function. Now, your function does not work, because you never called it. Please see below the implicit duplicates are still there. So, please do not forget to call the function.
# 
# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 1</b> 
#     
# 
# The function looks good.

# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
#     
# Please fix the code errors here and below.
#     
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# However, you need to replace the values in `df` dataframe (not `df_clean`). 

# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# You don't need to repeat the same operations twice. 

# Make sure the duplicate names are removed. Print the list of unique values from the `'type'` column:

# In[21]:


# AMENDED BY REVIEWER

#unique_types = sorted(df['type'].str.lower().unique())
unique_types = sorted(df['type'].unique())

print(unique_types)


# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 3</b> 
# 
# Please note that I changed the code in the block above to see the current values (unmodified) in `type` column.
#     
# 
#     
# <strike>
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# After you correct the function call, please check here the new values in `df['type']` column.

# ### Conclusions <a id='data_preprocessing_conclusions'></a>
# We detected three issues with the data:
# 
# - Incorrect header styles
# - Missing values
# - Duplicate rows and implicit duplicates
# 
# The headers have been cleaned up to make processing the table simpler.
# 
# All rows with missing values have been removed. 
# 
# The absence of duplicates will make the results more precise and easier to understand.
# 
# Now we can move on to our analysis of the prepared data.

# ## Stage 3. Data analysis <a id='hypotheses'></a>

# Based on the previous project stages, you can now define how the assumption will be checked. Calculate the average amount of votes for each score (this data is available in the `imdb_score` and `imdb_votes` columns), and then check how these averages relate to each other. If the averages for shows with the highest scores are bigger than those for shows with lower scores, the assumption appears to be true.
# 
# Based on this, complete the following steps:
# 
# - Filter the dataframe to only include shows released in 1999 or later.
# - Group scores into buckets by rounding the values of the appropriate column (a set of 1-10 integers will help us make the outcome of our calculations more evident without damaging the quality of our research).
# - Identify outliers among scores based on their number of votes, and exclude scores with few votes.
# - Calculate the average votes for each score and check whether the assumption matches the results.

# To filter the dataframe and only include shows released in 1999 or later, you will take two steps. First, keep only titles published in 1999 or later in our dataframe. Then, filter the table to only contain shows (movies will be removed).

# In[22]:


# Filter the dataframe to only include shows released in 1999 or later
df_filtered = df[(df['release_year'] >= 1999) & (df['type'] == 'SHOW')].copy()


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 3</b> 
#     
# ✔️ The two above blocks is currently correct.
#     
# <strike>
# 
# 

# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 3</b> 
# 
# I'm moving the following blocks down, where they need to be, so that they follow the instructions on how to deal with the outliers.

# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
#     
# Please check what is the correct type to which your replaced the implicit duplicates.
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 1</b> 
# 
# Could you please split the code in the cell above into several cells, keeping in the cell only what is requested by the task at the current step?
#     
# At this step you were only requested ___using conditional indexing modify df so it has only titles released after 1999 (with 1999 included)___
# 
# --- 
#     
# You are having the error because at the moment there are no `'type'` column in your `df` dataframe. I output the first lines of your `df` dataframe ad you can see that the column now is named `'____type'`/
#     
# ---- 
#     
# Following the instructions, please complete the project. If you have difficulties, please contact your Community Managers to have a meeting with a tutor.

# The scores that are to be grouped should be rounded. For instance, titles with scores like 7.8, 8.1, and 8.3 will all be placed in the same bucket with a score of 8.

# In[23]:


df_filtered['rounded_score'] = df_filtered['imdb_score'].round()


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 3</b> 
#     
# ✔️ OK, the rounding is correct.
#     
# <strike>
# 
# 

# It is now time to identify outliers based on the number of votes.

# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 4</b> 
# 
# Please see below how you need to group the dataset correctly and determine the outliers.
#     
# 
#     
# <strike>
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 3</b> 
# 
# There was an instruction here to identify the outliers the following way:
#     
# ___Use groupby() for scores and count all unique values in each group, print the result___
#     
# Could you please try to identify the outliers based on the instruction above?    
#     
# The three below code block are not required, so I commented them out.    

# In[24]:


vote_counts = df['imdb_votes'].groupby(df['imdb_votes']).count()
print(vote_counts)


# In[25]:


#ADDED BY REVIEWER

df_filtered.groupby('rounded_score').nunique()


# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
# 
# I did not find code for this step.

# Based on the aggregation performed, it is evident that scores 2 (24 voted shows), 3 (27 voted shows), and 10 (only 8 voted shows) are outliers. There isn't enough data for these scores for the average number of votes to be meaningful.

# To obtain the mean numbers of votes for the selected scores (we identified a range of 4-9 as acceptable), use conditional filtering and grouping.

# In[26]:


# filter dataframe using two conditions (scores to be in the range 4-9)
df_filtered_cond = df_filtered.loc[(df_filtered['rounded_score'] >= 4) & (df_filtered['rounded_score'] <= 9)]


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 3</b> 
#     
# ✔️ OK, well done, you've filtered the dataframe. 
#     
#     
#     
# <strike>
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
# 
# Please determine the outliers in the column with rounded scores (not in 'imdb_votes') and filter the dataframe from them. 

# In[27]:


#HELP HERE! I am getting an empty df with floats. I tried df vote_counts as well and it is 
#similarly empty. I am calling the right columns, but I am getting mixed up with which df
#and where the data is going. There was no transformation from int to float. Does this 
#happen with .round(). I just checked with .astype(int) and the df is still empty.

mean_votes_by_score = df_filtered_cond.groupby('rounded_score')['imdb_votes'].mean().astype(int).reset_index()
print(mean_votes_by_score)


# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 5</b> 
#     
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 4</b> 
# 
# The table is not empty now, it contains correct information.
#     
# Please add `.reset_index()` to change the series to dataframe again:
#     
# `mean_votes_by_score = df_filtered_cond.groupby('rounded_score')['imdb_votes'].mean().astype(int).reset_index()`  
#     
#     
# <strike>
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 3</b> 
# 
# Please determine the average number of votes for each rounded score in the block above.

# <strike>
# 
# 
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
# 
# This is not the case. There is a problem at a previous step due to which you got an empty dataframe.

# Now for the final step! Round the column with the averages, rename both columns, and print the dataframe in descending order.

# In[28]:


#HELP HERE! Which column exactly is being averaged? The instruction is not the most clear. is it
#imdb_votes and rounded_score?

# Round the average votes and rename columns
#mean_votes_by_score['new_rounded_score'] = df_filtered_cond['rounded_score'].astype(int)
#mean_votes_by_score['average_votes'] = df_filtered_cond['imdb_votes'].round().astype(int)
#average_votes_per_score = df_filtered_cond.rename(columns={'rounded_score': 'imdb_score', 'imdb_votes': 'average_votes'})

# Print the resulting DataFrame in descending order
#print(average_votes_per_score.sort_values('average_votes', ascending=False))


# In[30]:


# ADDED BY REVIEWER

# Rename the columns
mean_votes_by_score = mean_votes_by_score.rename(columns={'rounded_score': 'imdb_score', 'imdb_votes': 'average_votes'})

# Print the resulting dataframe in descending order
mean_votes_by_score.sort_values('average_votes', ascending=False)


# <div class="alert alert-warning"; style="border-left: 7px solid gold">
# <b>⚠️ Reviewer's comment, v. 5</b> 
# 
# Please see above - you needed to take the dataframe you created at the previous step, rename the columns and sort it.
#     
# I commented your code and showed correct option. Hope this helps.
#     
# <strike>
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 4</b> 
#     
# 1. Please note the you do not have a dataframe called `average_votes_per_score`, please specify correct dataframe name.
#     
# 2. You averaged the column with imdb_votes. So this is the column which you needed to round here. But you already changed its type to integer in the previous step, so there is no need to round it again.
#     
# 3. Please rename the columns and sort the dataframe, the one you created at the previous step.
#     
#     
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 3</b>
#     
# Please fix the code above to get the required result in line with the instructions.
# 
# <div class="alert alert-danger"; style="border-left: 7px solid red">
# <b>⛔️ Reviewer's comment, v. 2</b> 
# 
# Please do not forget the complete the step.

# The assumption macthes the analysis: the shows with the top 3 scores have the most amounts of votes.

# ## Conclusion <a id='hypotheses'></a>

# The research done confirms that highly-rated shows released during the "Golden Age" of television also have the most votes. While shows with score 4 have more votes than ones with scores 5 and 6, the top three (scores 7-9) have the largest number. The data studied represents around 94% of the original set, so we can be confident in our findings.

# <div class="alert alert-success"; style="border-left: 7px solid green">
# <b>✅ Reviewer's comment, v. 2</b> 
#     
# Overall conclusion is an important part, where we should include the summary of the outcomes of the project.
#     
# Please note that you will need to write one for every project you make.
