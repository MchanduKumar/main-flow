#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


data=pd.read_csv("H:\\ml lab\\householdtask3.csv")


# In[11]:


data.head(10)


# In[12]:


plt.scatter(data['year'],data['own'])
plt.title("Scatter Plot")
plt.xlabel('year')
plt.ylabel('own')
plt.show()


# In[13]:


plt.plot(data['year'])
plt.plot(data['own'])
plt.title("Line Chart")
plt.xlabel('year')
plt.ylabel('own')
plt.show()


# In[14]:


plt.bar(data['year'],data['own'])
plt.title("Bar Plot")
plt.xlabel('year')
plt.ylabel('own')
plt.show()


# In[15]:


plt.hist(data['income'])
plt.title("Histogram")
plt.show()


# In[ ]:





# In[ ]:




