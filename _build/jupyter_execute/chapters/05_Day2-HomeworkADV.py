#!/usr/bin/env python
# coding: utf-8

# ## **Day 2 Advanced Homework**

# Here is a [csv](https://github.com/ucdavisdatalab/python_intensive_training/tree/main/data/Day2CountryInfo2018_ADV.csv) file that contains all of the countires that medalled in the 2018 Winter Olympic games, their latitudes and longitudes, medals won, GDP (2018), and population (2018). This time, we are going to plot the countries with more information.

# # Initial Instructions:

# 1.   Download the csv file from the link above.
# 2.   Open a new [Google Colab notebook](https://colab.research.google.com/) and click on "New Notebook" in the corner.
# 3.   Click the file icon on the left toolbar, then click on the upload icon (the button on the left).
# 4.   Choose the new .csv file to upload in order to import the data.
# 5.   Here’s the actual homework!

# # Assignment

# 
# *   Open the csv file and examine what’s in it. What variable types are in here? Strings, floats, or integers?
# *   In your Colab notebook, write a script that imports the data from the file to make a scatter plot.
# *   As you parse the data, for each country you’ll need to tally up the total medals. You will also need to calculate GDP per 5000 capita (GPD per 5000 people).
#     *   What techniques that we have reviewed can we use to accomplish these?
# *   We will be plotting the countries that did not medal at all in a different color scheme than the rest of the countries. As you parse the data you will need find a way to sort out countries that did not medal.
# *   This time when you plot the data, color the countries according to number of medals won, and change the size of each point based on GPD per capita.
#     *   See the [plt.scatter()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html) documentation to try to figure out how to implement this.
#     *   For countries that did not medal, color them grey, but still change the size of the points with GDP per capita. (Hint: this may require a separate plt.scatter command)
# *   Add the equator to the plot.
# *   Congrats! You are all done.
# *   The plot contains more information than the map from Day 1. In Day 3 we will delve into using more libraries and do more data analysis.

# [.ipynb file](https://https://github.com/ucdavisdatalab/python_intensive_training/tree/main/data/HWDay2_ADV.ipynb)
# 
# [plot](https://https://github.com/ucdavisdatalab/python_intensive_training/tree/main/img/Day2_ADV_plot.png)

# In[ ]:




