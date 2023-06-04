#!/usr/bin/env python
# coding: utf-8

# # IPL 2017 DATASET ANALYSIS

# In[1]:


#loading a required library
import numpy as np
import pandas as pd
import seaborn as sbn
from matplotlib import pyplot as plt


# In[2]:


#loading ipl matches dataset
ipl=pd.read_csv('matches.csv')


# In[3]:


#view top 5 records in the dataset
ipl.head()


# In[5]:


#view total rows and tables in matches dataset
ipl.shape


# In[7]:


#getting the frequency of most man of the match award
ipl['player_of_match'].value_counts()


# In[9]:


#getting the top 10 players with most man of the match award
ipl['player_of_match'].value_counts()[0:10]


# In[10]:


#getting the top 5 players with most man of the match award
ipl['player_of_match'].value_counts()[0:5]


# In[11]:


# getting a top5 name of the players in man of the matche award
list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[13]:


#here we creat a bar chart of top 5 players who awarded in man of the match awarded
plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="g")
plt.title('TOP 5 PLAYERS')
plt.xlabel('Players Name')
plt.ylabel('Man Of The Match Award')


# In[15]:


#geting a frequency of result column
ipl['result'].value_counts()


# In[16]:


#finding out the records where who teams wins a toss
ipl['toss_winner'].value_counts()


# In[18]:


# Extracing the records where a team won bating first
batting_first=ipl[ipl['win_by_runs']!=0]


# In[19]:


#view top batting_first winners head
batting_first.head()


# In[21]:


#count of total wins matches by first bating
batting_first.shape


# In[30]:


#making a histogram of win by batting_first matche
plt.figure(figsize=(5,5))
plt.hist(batting_first['win_by_runs'],color='blue')
plt.title('Distribution of Runs')
plt.xlabel('Runs')
plt.show()


# In[31]:


#finding number of wins match after batting first
batting_first['winner'].value_counts()


# In[34]:


#making a bar plot for top3 teams who wins batting-first
plt.figure(figsize=(6,6))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=['blue','yellow','green'])
plt.show()


# In[38]:


#making a pie chart of top wins after batting-first
plt.figure(figsize=(5,5))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[39]:


# Extracting those recordes where a team has won after batting secccond
batting_second=ipl[ipl['win_by_wickets']!=0]
batting_second.head()


# In[45]:


# Making a histogram for frequencyof wins mattch numbers of wicket
plt.figure(figsize=(5,5))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[47]:


# Find a numbers of teams frequency who wins batting seccond
batting_second['winner'].value_counts()


# In[50]:


#creating a bar plot for top 3 team who wins after batting_seccond
plt.figure(figsize=(5,5))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=['green','yellow','blue'])
plt.show()


# In[52]:


# Creating a pie chart of winer teams who batting seccond
plt.figure(figsize=(5,5))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[54]:


# Find a numbers of matches playes in those seasion
ipl['Season'].value_counts()


# In[57]:


# Find a numbers of top 5 matches playes in those seasion
ipl['Season'].value_counts()[0:5]


# In[55]:


# Find a numbers of city where matches are played
ipl['city'].value_counts()


# In[56]:


# Find a numbers of top 5 city where matches are played
ipl['city'].value_counts()[0:5]


# In[58]:


# find a how many matches are win after winning toss
import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])


# In[59]:


# Finf a what ratio of if we win toss then we win matche
#first we found a number of matches
#and we divided into match win after toss win
ipl.shape


# In[61]:


# persont of win matches where we win a toss
393/756


# In[ ]:




