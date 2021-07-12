#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
#Further cleaning the flights dataset and splitting it into other sets


# In[45]:


flights=pd.read_csv('C:\\NSLC\\MajorSim\\atlFlights.csv')


# In[64]:


#Removes extraneous data columns
flights=flights[['MONTH','AIRLINE','ORIGIN_AIRPORT','DESTINATION_AIRPORT','DEPARTURE_TIME','ARRIVAL_TIME','AIR_SYSTEM_DELAY','SECURITY_DELAY']]
flights.value_counts('AIRLINE')


# In[66]:


#Creates a dataset of all flights arriving at hartsfield jackson,with relevant data
incomingFlights=flights[flights['DESTINATION_AIRPORT']=='ATL']
incomingFlights=incomingFlights.drop(['DESTINATION_AIRPORT','DEPARTURE_TIME','SECURITY_DELAY',],axis=1)
incomingFlights.to_csv('incomingFlights.csv')


# In[65]:


#Creates a dataset of all outbound flights from hartsfield jackson, with relevant data
outboundFlights=flights[flights['ORIGIN_AIRPORT']=='ATL']
outboundFlights=outboundFlights.drop(['ORIGIN_AIRPORT','ARRIVAL_TIME','AIR_SYSTEM_DELAY'],axis=1)
#outboundFlights.to_csv('outboundFlights.csv')


# In[24]:


flights.to_csv('atlFlightsUpdate.csv')

