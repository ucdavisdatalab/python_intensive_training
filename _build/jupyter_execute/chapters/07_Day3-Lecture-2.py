#!/usr/bin/env python
# coding: utf-8

# # **Day 3**

# ## Goals/Anti-goals

# * **Goal**: Provide a tour of several different libraries
# * **Goal**: Demonstrate the synergy of the "Python Universe"
# * **Goal**: Demonstrate paradigm "get idea then translate into code"
# * **Goal**: Demonstrate paradigm "write one line, test, then continue"
# 
# 
# 
# * **Anti-goal**: Teach specific functions and specific arguments
# * **Anti-goal**: Confuse you 

# ## Roadmap

# A) Obtain dataset from the internet
# 
# B) Prepare dataset for analysis with *pandas*
# 
# C) Cluster dataset with *sklearn*
# 
# D) Dimensionality reduction with *UMAP*, visualization with *matplotlib*
# 

# ## A) Obtain dataset from the internet

# #### Description: 

# * 23 species
# 
# * Coincidentally 23 features (columns)
# 
# * 8124 samples (rows)
# 
# * 11th column has missing data
# 

# #### Image of dataset:

# ![alt text](../img/day_3_lecture_2_image_1.png "Title")

# ## B) Prepare dataset for analysis using pandas

# * pandas 
# * library in python
# * perfect for matrix-like data of mixed types (numbers, strings, etc.)

# ### Overall Strategy

# 0) Get dataset into python
# 
# 1) Deal with missing data (drop column)
# 
# 2) Transform letters into numbers (one-hot encoding)

# ### 0) Get dataset into python

# * get pandas library
# * get a hard coded address for the file
# * try a simple usage of read_csv
# * check our work
# * update our usage of read_csv and check work again

# In[1]:


# get library
import pandas as pd


# In[2]:


# get a hard coded address for the file
mushroom_dataset_address='../data/agaricus-lepiota.csv'


# In[3]:


# try a simple usage of read_csv
my_Panda=pd.read_csv(mushroom_dataset_address)


# In[4]:


# check our work
my_Panda


# In[5]:


# update our usage of read_csv and check work again
my_Panda=pd.read_csv(mushroom_dataset_address,header=None)
my_Panda


# ### 1) Deal with missing data (drop column)

# 
# We need a fast and clear approach
# 
# *   use the function DataFrame.drop
# *   check our work
# 
# 

# In[6]:


# use the function DataFrame.drop
## labels indicates the "name" of the column to drop
## axis indicates whether we are dropping from columns or rows (10 exists on both)
## inplace means that we are modifying the variable my_Panda instead of getting a result returned
my_Panda_column_dropped=my_Panda.drop(labels=11,axis='columns')


# In[7]:


# check our work
my_Panda_column_dropped


# ### 2) Transform letters into numbers
# Why?

# #### Background: clustering

# 8,124 samples -> which samples come from the same species?
# 
# Clustering: Group datapoints based on location

# #### Image

# source:: https://miro.medium.com/max/1200/1*rw8IUza1dbffBhiA4i0GNQ.png
# 
# ![alt text](../img/day_3_lecture_2_image_2.png "Title")

# #### One-hot encoding

# To cluster, we need to put data points in spatial locations
# 
# Right now each datapoint has 23 letters
# 
# We use the strategy of "one-hot encoding"

# #### image

# source: https://miro.medium.com/max/875/1*ggtP4a5YaRx6l09KQaYOnw.png
# 
# ![alt text](../img/day_3_lecture_2_image_3.png "Title")

# #### Code

# In[8]:


# one hot encoding
## this time, we got a copy of the dataset back instead of operating on the variable my_Panda directly
## we specify what to encode using 'data'
## we provide a list of columns using my_Panda.columns - we could have also type the list [0,1,2,...,20,21,22]
my_Panda_dummies=pd.get_dummies(data=my_Panda_column_dropped,columns=my_Panda_column_dropped.columns)


# In[9]:


# check our work
my_Panda_dummies


# ## C) Cluster the data with sklearn

# ### Background: 

# In the above image, data had 2 dimensions so we could visually assess clustering
# 
# For n-dimensional case We turn to a clustering algorithm.
# 
# Within sklearn we choose the algorithm K-means.
# 
# Because time constraints we treat KMeans like a black box

# #### Image: Black box

# Black box: give input, get output, dont ask how
# 
# Step 1) 
# * Parameters: arguments that our chosen algorithm requires
# 
# Step 2) 
# * Input: my_Panda_dummies
# * Output: list of labels 
# 

# ![alt text](../img/day_3_lecture_2_image_4.png "Title")

# #### Giving parameters to K-means black box
# 
# KMeans *requires* the number of clusters (23)
# 

# In[10]:


from sklearn.cluster import KMeans


# In[11]:


#declare our black box by calling KMeans
##we give the black box/calculator the name my_KMeans_tool
my_KMeans_tool=KMeans(n_clusters=23)


# In[12]:


print(my_KMeans_tool)


# In[13]:


#we havent told my_KMeans_tool about our data yet, so we expect this to fail
print(my_KMeans_tool.labels_)


# #### Black Box Operation
# sklearn (often) relies on the function "fit_transform" to connect the data with the algorithm

# In[45]:


#tell my_KMeans_tool about our data
## we ignore the output
## notice how sklearn's KMeans flawlessly accepts a panda as input
my_KMeans_tool.fit_transform(X=my_Panda_dummies)


# In[46]:


#now we see that we have the labels that expected
print(my_KMeans_tool.labels_)
print(len(my_KMeans_tool.labels_))


# #### Done?
# 

# 
# Got a label for every data point.
# 
# Philosophical viewpoint: We did perfectly, the algorithm worked exactly as intended
# 
# Are our clusters meaningful?
# 
# Hard to say. We could try to relate our clusters to some external dataset. We don't have that here.
# 
# Lets try a visualization.
# 
# In our case, we are going to:
# * Take our 114 dimensional dataset (114 columns)
# * Reduce the dimensionality to 2.
# * Plot all datapoints, getting (x,y) from dimensionality reduction and colors from clustering label.
# 
# If each color of datapoints is separated from every other cluster, then we have some assurance that our dataset is "robustly clusterable". That's it.

# ## Dimensionality Reduction and Visualization
# 
# 

# #### Naive approach:

# choose two columns and drop all of the rest

# #### Which algorithm?
# 

# PCA, PLS-DA, t-SNE, UMAP
# 
# 

# demonstrate the bredth/synergy of the python language, so we choose UMAP (not in sklearn)
# 
# Even though UMAP is not in sklearn, the authors of UMAP wrote it in such a way that it "works like" sklearn functions.

# #### Strategy

# * create our UMAP black box
# * operate that black box on our dataset
# * obtain a 2-d coordinate pair for every datapoint
# * plot those pairs, with the color of the datapoint reflecting the clustering label from KMeans

# #### Code

# In[47]:


# create our black box
## import our library
import umap

## declare a couple of parameters that we wont get into
n_neighbors=10
min_dist=0.1
n_components=2
metric='euclidean'


##just like last time, we declare a "UMAP calculator" and send a couple of parameters
my_UMAP=umap.UMAP(n_neighbors=n_neighbors,min_dist=min_dist,n_components=n_components,metric=metric)


# In[48]:


print(my_UMAP)


# In[49]:


# again, we use fit transform to inform our calculator of our dataset 
## again, notice how it flawlessly accepts a panda
## this time, we actually want the thing that gets spit back out
my_UMAP.fit_transform(my_Panda_dummies)


# We redo to capture the 2D coordinate list

# In[50]:


# 2) and 3)
my_numpy_2d=my_UMAP.fit_transform(my_Panda_dummies)
print(len(my_numpy_2d))


# In[51]:


import matplotlib.pyplot as plt


# In[52]:


#4)
#scatter plot takes
#list of x coordinates
#list of y coordinates
plt.scatter(
    my_numpy_2d[:,0],
    my_numpy_2d[:,1]
)
plt.show()


# In[53]:


#4) redo with arguments to make the color in accordance wiht the KMeans cluster labels



#an opacity parameter
plt.scatter(
    my_numpy_2d[:,0],
    my_numpy_2d[:,1],
    #a label list
    c=my_KMeans_tool.labels_,
    #a color bar (literally the rainbox)
    cmap='gist_rainbow',
    #make the points mildly transparent so we can see generalities
    alpha=0.2
)
plt.show()


# #### Observations
# Our dimensionality reduction technique independently produced 23 visually-discernible clusters, but those clusters only partially agree with the KMeans clustering

# #### Bonus: Dim Reduction with PCA

# In[54]:


import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
my_PCA=PCA()
my_PCAd_coordinates=my_PCA.fit_transform(my_Panda_dummies)
plt.scatter(range(len(my_PCA.explained_variance_ratio_)),my_PCA.explained_variance_ratio_)
plt.show()
print(my_PCAd_coordinates.shape)
print(my_PCAd_coordinates[:,0].shape)
plt.scatter(my_PCAd_coordinates[:,0],my_PCAd_coordinates[:,1],c=my_KMeans_tool.labels_,cmap='gist_rainbow',alpha=0.2)
plt.show()

