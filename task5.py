#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('H:\\datasets\\heart.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.columns.values


# In[6]:


df.isna().sum()


# In[7]:


df.info()


# In[8]:


#histogram of all numeric values
df.hist(bins=50,grid=False,figsize=(20,15));


# In[9]:


df.describe()


# In[10]:


ques=["1. How many people have heart disease and how many people doesn't have heart disease?",
      "2. People of which sex has more heart disease?",
      "3. People of which sex have which type of chest pain?",
      "4. People of which chest pain are mmost pron to have heart disease?"]
ques


# In[11]:


#to find the ans of first ques
#getting the values

df.target.value_counts()


# In[12]:


#plotting bar chart
df.target.value_counts().plot(kind='bar',color=["orchid","salmon"])
plt.title("Heart Disease Values")
plt.xlabel("1= Heart Disease,0= No heart Disease")
plt.ylabel("Amount");


# In[13]:


#plotting pie chart
df.target.value_counts().plot(kind='pie',figsize=(8,6))
plt.legend(["Disease","No disease"]);


# In[14]:


# o for Female
# 1 for male
# sex column  part
#0 represent no disease
# 1 for disesase
#target column part

df.sex.value_counts()


# In[15]:


#plotting pie chart

df.sex.value_counts().plot(kind='pie',figsize=(8,6))
plt.title('Male Female ratio')
plt.legend(['Male','Female']);


# In[16]:


#for 2 ques

pd.crosstab(df.target,df.sex)


# In[17]:


sns.countplot(x='target',data=df,hue='sex')
plt.title("Heart Disease Frequency for sex")
plt.xlabel("0=No heart disease,1= Heart disease");


# In[18]:


#3

df.cp.value_counts()


# In[19]:


df.cp.value_counts().plot(kind='bar',color=['salmon','lightskyblue','springgreen','khaki'])
plt.title('chest pain type vs count');


# In[20]:


pd.crosstab(df.sex,df.cp)


# In[21]:


pd.crosstab(df.sex,df.cp).plot(kind='bar',color=['coral','lightskyblue','plum','khaki'])
plt.title("Type of chest pain for sex")
plt.xlabel('0=Female,1=Male');


# In[22]:


#4

pd.crosstab(df.cp,df.target)


# In[23]:


sns.countplot(x='cp',data=df,hue='target');


# In[28]:


sns.displot(x='age',data=df,bins=30,kde=True);


# In[26]:


sns.displot(x='thalach',data=df,bins=30,kde=True,color='chocolate');


# In[ ]:




