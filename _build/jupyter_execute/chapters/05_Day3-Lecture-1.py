#!/usr/bin/env python
# coding: utf-8

# # **Day 3**

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pprint import pprint


# ## What is a pandas DataFrame

# * Pandas is a library 
#     * (import it, has a documentation website https://pandas.pydata.org/)
#     
# * DataFrame is a datatype/datastructure/object
#     * the main offering of the pandas library
#     
# * Pandas DataFrame 
#     * Robust tool for data wrangling and data analysis
#     * Exceptionally good documentation
#     * Synergizes with other Libraries
#     
# * Use-case/motivation
#     * More convenient than numpy arrays
#     * More powerful than excel
#     * In-memory amount of data
#     * Millions of rows 

# ## Clear example of DataFrame

# ![alt text](../img/day_3_lecture_1_image_1.png "Title")

# * Column Indexes
# * Row Indexes
# * Multiple datatypes
# * Datatypes function of column
#     * List of strings in the entry at [4,'column_three']

# ## How can we make a DataFrame?

# * read in a .csv file
# * from a python dictionary
# * from a pickle (special binary file)
# * from json
# 
# the list goes on
# 

# ## Making the above DataFrame

# Strategy: DataFrame from a python dictionary (less common, but helpful for now)
# 
# 
# We make a dictionary where 
# * the keys are column names
# * the values are lists of actual data

# In[2]:


#make the values
first=[1,2,3,4,5]
second=['a','b','c','d','e']
third=['lets','mix','it','up',['ok']]


# In[3]:


#assign the values to keys in a dictionary
my_dict={
    'column_one':first,
    'column_two':second,
    'column_three':third
}


# In[4]:


#print the whole dictionary to see what it looks like
#note that the keys are ordered alphabetically when we use pprint (pretty print)
pprint(my_dict)


# In[5]:


#declare our dataframe using the "from dictionary approach"
my_DataFrame=pd.DataFrame.from_dict(my_dict)


# In[6]:


#see our dataframe
my_DataFrame


# ## Accessing Values in a dataframe

# ### Accesing the Indices (indexes)

# The indices are accessible and mutable (changeable)

# In[7]:


print(my_DataFrame.index)
print(my_DataFrame.columns)


# Pandas has many functions that operate-on and/or accept indexes
# 
# We can also use the column indices to access columns (a column is called a "series") in some contexts

# In[8]:


my_DataFrame['column_three']


# ### Accesing by numeric location

# DataFrames can be accessed like traditional lists (according to numerical position).
# 
# This can be a mildly dangerous approach if you are writing for long-term projects

# In[9]:


my_DataFrame.iloc[2,1]


# ### Accessing by index

# "at" is a good choice for single-value access

# In[10]:


my_DataFrame.at[2,'column_three']


# "loc" is a good choice for "slicing" a dataframe
# (provide a list of row-indexes and a list of column-indexes)

# In[11]:


my_DataFrame.loc[0:2,['column_two','column_three']]


# ### Accessing by condition

# loc is a good choice for choosing subsets based on a condition
# we can place the conditions where we placed lists earlier using loc
# (fyi: under the hood, python turns the condition into a list of True/False)

# In[12]:


my_DataFrame.loc[
    my_DataFrame['column_one'] > 2
]


# ## Operations on a DF

# ### Simple Operations

# Taking the average of a column
# Adding a constant to a column
# Stripping the whitespace from the ends of strings in a column
# 
# General advice = There is a built-in function for this. It will be fast and error free (assuming that the result is tested, etc). Google your needs and use the reusults

# In[13]:


my_DataFrame.column_one.mean()


# In[14]:


my_DataFrame.column_one+5


# In[15]:


#notice in the above we did not assign the output of "my_DataFrame.column_one+5" to anything.
#so the original dataframe remains unchanged
my_DataFrame


# In[16]:


#certain methods that operate on strings require accessing the string representation
#of the data stored in a colum
my_DataFrame.column_two.str.strip()


# ### More Complicated Operations

# General advice: certain operations are difficult/impossible to express using built-in functions. Especially if the project does not call for it, do not break your back to force the use of fast functions.
# 
# Instead, consider doing things "element-wise" "in a for-loop"
# 
# Example: each element in a column is searched against a database

# In[17]:


#iterrows gives us two things that we iterate over simultaneously, much like enumerate() on a
#"normal" list
for temporary_index,temporary_row in my_DataFrame.iterrows():
    #here, we just print because we dont want to write some weird function for the purposes
    #of demonstration.
    print(temporary_row['column_one']+3)


# ## Wrangling and Synergies with other libraries

# ### Getting a larger dataset

# In[18]:


#from https://github.com/ageron/handson-ml2/blob/master/02_end_to_end_machine_learning_project.ipynb
import os
import tarfile
import urllib.request

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


# In[19]:


fetch_housing_data()


# In[20]:


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# In[21]:


housing_dataset = load_housing_data()


# In[22]:


housing_dataset


# ### Basic inspection

# In[23]:


housing_dataset.info()


# In[24]:


housing_dataset.describe()


# In[25]:


#we can confirm our observation about the missin values using other functions
#great point - there are often many ways to do the same thing
#null inspects for the value "np.nan" which is numpy's null
#clearly, this operated on a cell-by-cell basis
housing_dataset.isnull()


# In[26]:


#we can sum the number of trues (think of it as adding the number of 1s and 0s)
#pandas generally operates on a per-column basis
housing_dataset.isnull().sum()


# We see what we saw, again

# Normally, we might consider imputing missing values. for the purposes of this exercise, we will just delete the rows that contain missin values.
# 
# 
# Alternative strategies to just removing them include 
# * passing a view with the missing values not present
# * recognizing that some functions accept a "skip na" argument

# In[27]:


#here we provide a condition like we saw up above
housing_dataset=housing_dataset.loc[
    housing_dataset.total_bedrooms.isnull()==False,
    #it is very important to provide the : as an indicator to choose all rows.
    #in this way, we avoid a view vs copy error
    :
]


# In[28]:


#we check our work
housing_dataset


# Notice how the #rows no longer matches index

# In[29]:


housing_dataset.reset_index(
    inplace=True,
    drop=True
)


# ### Checking scatterplots and histograms

# In[30]:


sns.pairplot(
    housing_dataset,
    #seaborn is built "on top of matplotlib", which means that it does a lot of things
    #more easily for you
    #however, some of the stuff in matplotlib is still accessible if you can express
    #what you want the same way.
    #here, we want the alpha parameter of scatter, which sets the opacity/transparency
    #of dots
    plot_kws={'alpha':0.5}
)


# In[31]:


#make you aware that you can do things like adjust color based on a column's value
sns.pairplot(
    housing_dataset[['longitude','latitude','total_rooms','median_income']],
    hue='median_income',
    palette='magma',
    #what does it mean have a histogram 
    diag_kind=None
)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




