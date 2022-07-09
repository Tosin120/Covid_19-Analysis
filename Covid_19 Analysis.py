#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[25]:


import pandas as pd


# In[26]:


#importing the data into jupyter note 
data = pd.read_csv(r'C:\Users\USER\Videos\New folder (8)\New folder\New folder\python files\4. covid_19_data.csv')


# In[27]:


data


# In[28]:


data.count()
# Null values means missing values


# In[29]:


#null values per column
data.isnull().sum()


# In[30]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[31]:


#heatmap showing the null values in the data
sns.heatmap(data.isnull())
plt.show()


# In[32]:


#the number of confirmed, deaths, and recovered cases in each region


# In[33]:


data.head(2)


# In[34]:


#the number of confirmed, deaths, and recovered cases in each region
data.groupby('Region').sum()


# In[35]:


#the number of confirmed cases in each region in a descending order
data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False)


# In[36]:


#the number of confirmed & Recovered cases in each region
data.groupby('Region')['Confirmed','Recovered'].sum()


# In[ ]:





# In[37]:


#remove all cases where confirmed cases are less than 10


# In[38]:


data.head(2)


# In[39]:


#highlighting confirmed cases less than 10
data[data.Confirmed > 10]


# In[42]:


# '~' is use to remove records satisfying a particular condition
data[~data.Confirmed > 10]


# In[43]:


data


# In[ ]:


#region where maximum of number of Confirmed cases were recorded


# In[44]:


data.head(2)


# In[48]:


# Top 20 regions where maximum of number of Confirmed cases were recorded
data.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20)


# In[ ]:


# Regions with minimum number of Death cases were recorded


# In[49]:


data.head(2)


# In[51]:


#Regions with minimum number of Death cases were recorded
data.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50)


# In[ ]:


# How many Confirmed, Death & Recovered cases are recorded from india, US & Yemen


# In[52]:


data.head(2)


# In[55]:


data[data.Region == 'India']


# In[57]:


data[data.Region == 'US']


# In[58]:


data[data.Region == 'Yemen']


# In[ ]:


# The entire data with respect to number of Confirmed cases in ascending order 


# In[59]:


data.head(2)


# In[62]:


#The entire data with respect to number of Confirmed cases in ascending order(first 50) 
data.sort_values( by = ['Confirmed'], ascending = True).head(50)


# In[ ]:





# In[ ]:


#The entire data with respect to number of recovered cases in descending order 


# In[63]:


data.head(2)


# In[64]:


#The entire data with respect to number of recovered cases in descending order(first 50) 
data.sort_values( by = ['Recovered'], ascending = False).head(50)


# In[ ]:




