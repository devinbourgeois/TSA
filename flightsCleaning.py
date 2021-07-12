#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[43]:


flightsData=pd.read_csv('C:\\NSLC\\MajorSim\\flights.csv')


# In[41]:


flightsData=flightsData[flightsData['Z']==True]


# In[42]:


flightsData.to_csv('atlFlights.csv')

