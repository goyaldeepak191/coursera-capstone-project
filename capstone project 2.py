#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


import numpy as np


# #set url for toronto postal codes

# In[12]:


url="https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"


# #Read data

# In[13]:


datau = pd.read_html(url, header=0)
data = datau[0]
data


# #NaN Neighbourhoods

# In[16]:


print("number of NaN values for the column Neighborhood :", data['Neighborhood'].isnull().sum())


# #Removeing all rows where Borough is not assigned

# In[17]:


data = data[data['Borough'] != 'Not assigned']
data 


# # Again checking NaN rows

# In[20]:



print("number of NaN values for the column Neighborhood :", data['Neighborhood'].isnull().sum())


# In[21]:


data.shape


# # Question 2 use the geocoder package or csv file to create dataframe with longitude and lattitudes

# In[22]:


location=pd.DataFrame(pd.read_csv('https://cocl.us/Geospatial_data'))
location


# ##### merging two tables for getting altitudes and lattitudes and various neighbours in one table

# In[24]:


data1= pd.merge(data,location[['Postal Code','Latitude','Longitude']],on='Postal Code')
data1


# #### taking data of toronto from borough for clustering and plotting

# In[25]:


Toronto = data1[data1['Borough'].str.contains('Toronto',regex=False)]
Toronto.reset_index(drop=True)


# In[ ]:




