#!/usr/bin/env python
# coding: utf-8

# # **UC Davis Python Intensive Training** 
# *Maggie Berrens and Parker Bremer*

# # *Overview*

# This three-day course is designed to prepare incoming (or experienced) graduate students and post docs with little to no coding experience for the coding demands that many graduate courses and research often requires. In the past this training was fully run by graduate students held over zoom or in a random classroom. This year we have teamed up with the UC Davis Data lab, who have offered their assistance in running the workshop and providing space for the workshop to take place. With that being said this intensive training is still majorly put together and run by graduate students and post docs aimed to help other graduate students and post docs. The intensive training will take place over September 6th - 8th from 5 pm - 7 pm with limited seating on campus in the Shields 360 (DataLab classroom) as well as on Zoom for those who don't obtain a spot for in person. This is a great opportunity to learn a new skill and meet other graduate students! Each session will begin with about an hour of demonstration to teach fundamental Python topics. This will be followed by time where studetns can work on an assignment with each other and ask questions to volunteers. The assignment each day will build off the previous sessions so by the end you will have a complete Python project!

# Any questions about the content of this site should be directed to Maggie Berrens (mlberrens@ucdavis.edu) or Parker Bremer (parkerbremer@ucdavis.edu)

# # Getting Started

# There are multiple ways to use Python. For this workshop no downloads will be necessary - all programming will be done in a browser using Google Colab. However, if you would like to download Python onto your computer and work offline, instructions will be provided below.

# Make sure you are logged-in on your browser with a Google account. Cick here to open a [new Google Colab notebook](https://colab.research.google.com/). Google Colab will save your files in your Google Drive. Select “New Notebook” at the bottom of the pop-up window. During the presentations, you can follow along and copy what is being demonstrated in your own file and run the code yourself. Here is a [brief introduction to some of Colab’s functionalities](https://www.youtube.com/watch?v=oCngVVBSsmA). If you don’t understand everyting that’s alright. Most importantly, pay attention to the difference between code and text cells, how to run cells of code, and how to move them around.
# 
# Note: We will be using Python 3 (the latest version of Python) for this workshop.

# # Homework Project

# Python is very versatile in its applications. The homework will focus on implementing fundamentals introduced in the lectures, working with data, and accessing Python libraries. There will be two homework levels, a standard assignment and an advanced assignment for those that want a challenge. The overall goal of the assignments will be to process data from the 2018 Winter Olympic Games and analyze what factors contribute to success. With the tools we learn, we can even create a model that tries to predict Olympic success in other years!

# # Agenda

# Attendees can either follow along throughout the training using this reader where all of the lectures and homeworks are posted. Or attendees can code in live time by following along as instructors also live time code using google colab

# ## **Day 1**: [Lecture File](https://github.com/ucdavisdatalab/python_intensive_training/tree/main/data/Day1_Lecture.ipynb) 
# 
# * Introduction: What are Coding and Python?
# * Variables, Basic Operations and Print
# * Lists
# * Loops
# * NumPy
# * Basic Plotting
# * Data Importing Day1example.dat
# * Resources
# 
# ## **Day 2**: [Lecture File](https://github.com/ucdavisdatalab/python_intensive_training/tree/main/data/Day2_Lecture.ipynb) 
# * Indexing lists
# * Arrays
# * Conditionals
# * Nested Loops
# * Functions
# * More Plotting 
# 
# 
# ## **Day 3**: [Lecture File](https://github.com/ucdavisdatalab/python_intensive_training/tree/main/data/Day3_Lecture.ipynb) 
# 
# Real research application of Python:
# * Finding Other and Using Other Libraries
# * Pandas, Sklearn, UMAP
# * Thought Process of Coding and Data Processing
# 
# 

# # Additional Resources
# 

# ## **Microcredential**
# 

# At the start of the workshop on Sept. 6th 5 pm we will have Pamela Reynolds from the DataLab briefly introduce how along with attending this training attendees have the possibility to earn a python microcredential through the university with some additional outside learning. It is important to emphasize that many of the skills learned in the intensive training will be covered in the microcredential but to the extra skills needed to earn the microcredential will require indpendent learning. More information regarding what the microcredential is and what is involved to earn the python badge can be found [here](https://datalab.ucdavis.edu/2021/10/20/announcing-pathway-research-computing/)

# ## **Downloading Python Offline**

# One of the easiest ways to download python is through Anaconda. Anaconda is a Python distribution that has extra feautres and packages that make Python easier to use.
# *   [Anaconda Installation Documentation](https://docs.anaconda.com/anaconda/install/)
# *   Find your operating system in the list, follow the instructions.
# *   Find where your Anaconda-Navigator was installed located on your computer, open it.
# *   We recommend using Spyder to run Python
# Unlike Colab, there will be one text document without multiple cells (cells can be created). These files are saved as “.py” files instead of “.ipynb” and lack text boxes. The code syntax will be the same as Colab. To run the code, click the green “play” button at the top - all of the code in the document will be run at once instead of just a single cell.

# ## **While Loops**
# 
# 
# 

# We did not talk about while loops in this course, but they also have their own useful purposes, often times with a conditional.
# - Not that infinite loops (getting stuck in a while loop without a way to exit) are a risk when using them!

# ## **Classes**
# 

# 
# - If you followed along through Day 3, we've hinted at the idea of object oriented programming and classes. There was not enough time to cover them in this workshop, but if you continue to explore Python they will be incredibly useful to understand and know how to implement.
# 

# ## **Code of Conduct**

# All participants must abide by our Code of Conduct

# Python Intensive Training is neither a dating scene nor an intellectual contest.
# 
# Python Intensive Training is dedicated to providing a harassment-free experience for everyone, regardless of gender, gender identity and expression, age, sexual orientation, disability, physical appearance, body size, race, or religion (or lack thereof). We do not tolerate harassment of participants in any form. Sexual language and imagery is generally not appropriate.

# Harassment includes offensive verbal comments related to gender, gender identity and expression, age, sexual orientation, disability, physical appearance, body size, race, religion, sexual images in public spaces, deliberate intimidation, stalking, following, harassing photography or recording, sustained disruption of talks or other events, inappropriate physical contact, and unwelcome sexual attention.
# 
# Attendees asked to stop any behavior are expected to comply immediately.
# 
# If you are being harassed, notice that someone else is being harassed, or if you are uncertain whether someone’s behavior might constitute harassment or have any other concerns, please contact any of the helpers, lead instructors, or organizers immediately.
# 
# Illegal actions may be reported to UC Davis Campus Police or other authorities.

# In[ ]:




