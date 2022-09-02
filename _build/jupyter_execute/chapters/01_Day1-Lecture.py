#!/usr/bin/env python
# coding: utf-8

# # **Day 1**
# 
# 

# ## **Why Coding and Python?**
# 
# 
# 
# *   Great for data processing and simulations
# *   Coding is fast at dealing with large amounts of data and math
# *   Python, very versatile and popular
# *   Very active community developing libraries for it
# *   One of the more user beginner friendly languages
# *   Skills transfer to other languages
# 
# 
# The goal of this workshop is to teach you the practical basics and fundamentals, but also show you how to access resources and teach yourself.
# 
# 

# ## Part 1: Variables
# 
# Variables are at the core of coding. Each variable contains a piece of data once assigned.
# 
# Types
# 
# 
# *   Integers
# *   Floats (decimals)
# *   Strings (text)
# 
# 

# In[1]:


a = 4
b = 4.0
c = 'four'
examplevariable = 54


# To see what code does, we need a way for it display information to us. That's the `print()` function. Whatever goes in the parentheses will be printed out for us. Notice that even though I inputted 'b' below, it showed us `4.0` instead of `b`. That's because we assigned `b` as a variable above:

# In[2]:


print(b)


# Alternatively, we can directly tell the Python to print the float 4.0:

# In[3]:


print(4.0)


# `print` is what we call a function in Python. It takes an input then perfroms an action. We'll learn more about those tomorrow.
# 
#  If we wanted to actually print 'b' instead of what we have assigned it to, we can directly put the string into the function:

# In[4]:


print('b')


# By putting quotes around it, 'b' is no longer a variable and is now just text part of a string. The `print` function is incredibly useful in outputting data, debugging, and developing. As a final note, print can output multiple variables or objects with one command:

# In[5]:


print(a,b,c, examplevariable)


# In[6]:


print('The value of b is',b)


# In[7]:


print(b,'is spelled',c)


# Finally, we can change variable types using the following functions:
# 

# In[8]:


var = 7.2
print(var)
print(int(var))
print(str(var))


# Variables can contain numbers, but not start with them!

# In[9]:


2014total = 2
print( 2014total )


# ## Part 2: Operations and Basic Math
# With integers and floats we can perform a lot basic math with Python:
# 
# 

# In[ ]:


s = 4
t = 9

added = s + t
print(added)
subtracted = s - t
print(subtracted)
multiplied = s * t
print(multiplied)
print(t*s)
print(t/3)
print(t**2)


# Python will follow the basic order of operations, so use parentheses ot accomplish what you want:

# In[ ]:


print( t**1/2 )
print( t**(1/2))


# As a note, floats and integers can be operated together even though they are different variable types.

# In[ ]:


m = 8.0
n = 2
o = '4'

print(m+n)
print(m+o)


# Be careful when re-assigning variables! If a variables is assigned a second time, it will overwrite the first.

# In[ ]:


m = 6
p = m+n
print(p)


# However, variables are not inherently linked. In the example below, when we assigned `r`, it is equal to `m + n` (6 + 2). Even though we change `m = 5` in the next line, `r` is still 6 + 2.
# 

# In[ ]:


r = m + n
print(r)
m = 5
print(r)
r  = m + n
print(r)


# ## Part 3: Lists
# 

# Lists are one of many ways to store multiple pieces of data. Use `[]` to create them and separate data with commas. 

# In[ ]:


mylist = [a, b, c]
print(mylist)
mylist2 = [4, 4.0, 'four']
print(mylist2)


# Most of the time, everything in your list will be the same variables type. Using the `append()` function you can add more to your list.
# 
# 

# In[ ]:


mylist.append('five')
print(mylist)


# Unfortunately, operations don't work as you would expect them to with lists.

# In[ ]:


list1 = [1,2,3,4,5]
list2 = [2,2,2,2,2]

print(list1+list2)
print(list1*3)


# How can we do math with lists then? We first need to talk about indexing lists and loops. If we only want a specific piece of data in a list, we have to use it's index.

# In[ ]:


months = ['jan','feb','march','april','may']
print(months[3])


# In[ ]:


print(list1[0]+list2[0])


# So now, for each element in the list, I could manually add them together with each index. That sounds like a lot work though. This is where loops are helpful.

# ## Part 4: Loops
# Loops are an essential part of coding. Many times, there is an operation we want to repeat over and over. Loops help us accomlish this. As we saw with `mylist` above, we can't perform math on lists. But we can "loop" over each individual element and perform the math. This is called a for loop.

# In[ ]:


list3 = [4,7,4,6,3]

newlist = []

#This line basically says, go over each element in list3 and assign that element to i
#So, the first iteration, i is equal to 4, then 7, and so forth
for i in list3:
  newlist.append(i*3)
  print (newlist)


# Another way to make for loops is by iterating over a range of numbers. This lets us loop over the index of multiple lists:

# In[ ]:


list1 = [1,2,3,4,5]
list2 = [2,2,2,2,2]

#We need to create an empy list before we can append anything to it.
addedlist = []

#This time, by looping over a range, i will be 0 the first iteration, and increase by one each time.
for i in range(5):
  print(i)
  #The next line effectively adds the corresponding elements of list1 and list2 together
  #ie, the first element of list1 is added to the first element of list2, the second element of list1 is added to the second element of list2
  addedlist.append(list1[i] + list2[i])

print(addedlist)


# In[ ]:





# Time permitting: review the `len()` function. If you put a list into the `len()` function, it will tell you how many elements are in that list. Using this, the for loop can detect the length of your list automatically to set the number of iterations.
# 

# In[ ]:


print(len(list1))


# In[ ]:


addedlist = []
for i in range(len(list1)):
  print(list1[i] + list2[i])
  addedlist.append(list1[i] + list2[i])

print(addedlist)


# Note, this is not the fastest way to add lists together but we will get more into that Day 2.

# ## Part 5: Basic NumPy
# Numpy is a mathematical based library with extra capabilities. Libraries are "add-ons" developed by other programmers. They add extra functions and capabilities. To import NumPy use the command below:

# In[ ]:


import numpy as np


# Now whenever we want to use a NumPy command, refer to it with `np.`

# In[ ]:


k = np.log(2)
print(k)

l = np.sqrt(100)
print(l)


# `np.linspace`  can be a useful tool. It creaes an array (similar to a list but more on that tomorrow) that starts and stops at the first 2 numbers. The third number you input contains the total number of elements evenly spaced.

# In[ ]:


numbers = np.linspace(0, 100, 51)
print(numbers)


# ## Part 6: Simple Plotting
# 

# Similar to NumPy, plotting also requires a library. Here is how you import it:

# In[ ]:


import matplotlib.pyplot as plt


# So any commands we need to do with plotting will have to use `plt.` first. For now, let's just show 2 basic types of plots. Create some arbitrary x values and y values to plot. Then, it's just a matter of plugging in the values into the correct functions and displaying the graph.

# In[ ]:


x = np.linspace(0, 50, 21)
y = np.linspace(30,40, 21)

#for a line plot:
plt.plot(x,y)
#display graph command
plt.show()


# In[ ]:



#for a scatter plot
plt.scatter(x, y)
#Show plot
plt.show()


# ## Part 7: Importing Data

# You always want to look at the file you're importing first. First we need to upload the file to our notebook. Click the file icon to the left toobar on Google Colab, and then click to upload button. Choose "Day1example.dat" from your computer.
# 
# What does it contain? With the "Day1example.dat" file, be can see that the first row contains two headers, and the rows after contain random floats. How can we import this data to use?
# 
# Now lets get into the code:
# 

# In[ ]:


#We need to create empty lists to store data:
xvals = []
yvals = []

#This line opens up the file. Make sure the include quotes around Day1example.dat to make it a string.
#otherwise Python will think Day1example.dat is some sort of variable.
#The 'r' in the open function tells Python we want to read this file. 
#The 'as infile' portion assings the text in the file to the variable infile.
with open('Day1example.dat','r') as infile:

  #We don't care about the first line, so to read over it and move on use this command
  headers = infile.readline()
  #Let's make sure it got rid of what we wanted
  print(headers)
  
  #Let's loop over the rest of the lines. The open command once it has read a line will get rid of it so we don't need to worry about that first line anymore.
  for line in infile:
    #This command splits up each line at every space. 
    #If we entered some text (string) into the parentheses of split(), then it would separate the lines
    #at every instance of that text (for a comma separated file, we would want line.split(',') )
    data1, data2 = line.split()
    
    #add the data to the lists. 
    #IMPORTANT: any text read from a file is a string. We must convert it floats to perform any plotting or math
    xvals.append(float(data1))
    yvals.append(float(data2))


#Plot Them!
plt.scatter(xvals, yvals)
plt.show()

