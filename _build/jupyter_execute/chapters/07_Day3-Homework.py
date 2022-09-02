#!/usr/bin/env python
# coding: utf-8

# ## **Day 3 Homework**

# Here is a [csv](/python_intensive_training/data/Day3CountryInfo2018.csv) file that contains all of the countires that medalled in the 2018 Winter Olympic games, their latitudes and longitudes, medals won, GDP (2018), and population (2018). Today we are going to focus on using different packages tto analyze the data. We want to see which factor affect Winter Olympic success (medal count) the most.

# # Initial Instructions:

# 1.   Download the csv file from the link above.
# 2.   Open a new [Google Colab notebook](https://colab.research.google.com/) and click on "New Notebook" in the corner.
# 3.   Click the file icon on the left toolbar, then click on the upload icon (the button on the left).
# 4.   Choose the new .csv file to upload in order to import the data.
# 5.   Here’s the actual homework!
# 

# # Assignment

# *   Your solution for Day 2 should already be able to parse all of the data from the file.
# *   Let’s examine three factors: GDP per capita, latitude, and raw population, and see how each of these affects medal results. While this is a complex question, we are going to assume a linear relationship for the sake of simplicity.
# *   Let’s start with GDP per capita. There are many ways to do this next step, but one of the easiest is to import the `scipy.stats` package and use the `linregress()` function
# ```
#  import scipy.stats as ss
# ```
#      *     Take a look at the documentation for [linregress](https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.stats.linregress.html). Particularly the examples may help.
#      *     What should we input into the function? What will be the output and how many should we expect?
# *   Once you have successfully fit the function, we need to plot our results. Make a scatter plot with the x (GDP per capita) and y (medal total) values.
# *   To the scatter plot, let’s add our fit line. 1) To do this you will need to define a linear function. Note, the order of the variables will be important. 2) Create an array of x values to plot (np.linspace() may be helpful) and input them into the function you just wrote. 3) Make sure you are using the slope and intercept generated from the ss.linregress(). 4) To make a line instead of a scatter plot, the plt.plot() function will be useful
# *    Print out the R squared value as well.
# *    Now we have a visualization for the realtionship between GDP per capita and Olympic medals!
# *    Repeat this process (you can copy and paste most of your work here and just change the data you use) for latitude and population
# *    Based on the results, which of these facotrs seems to be most impactful on Winter Olympic success?
# *    Congrats, you’ve successfully learned to use Python to parse, plot, and statistically analyze data! This is the end of the Python Bootcamp base project. 

# # Answer

# [.ipynb file](https://github.com/ucdavisdatalab/python_intensive_training/tree/main/data/HWDay3.ipynb)

# In[ ]:





# In[ ]:




