#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd

ftd = pd.read_excel('Atlanta_flights_test_size.xlsx')
#fill null
ftd = ftd.fillna(0)

'''get rid of repeat data
function works with parameters dataframe (what you want to delete from)
and column_name (what column you want to check for duplicates)
'''

def deleteRepeats(dataframe, column_name):
    dataframe.drop_duplicates(column_name, 'last',inplace=True)
    return dataframe
deleteRepeats(ftd, 'FLIGHT_NUMBER')


# In[ ]:





# In[ ]:




