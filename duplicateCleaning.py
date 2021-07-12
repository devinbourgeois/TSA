import numpy as np
import pandas as pd

ftd = pd.read_excel('Atlanta_flights_test_size.xlsx')
#reads the data from 'Atlanta_flights_test_size.xlsx'
ftd = ftd.fillna(0)
#fills null (NaN) values with 0
def deleteRepeats(dataframe, column_name):
    dataframe.drop_duplicates(column_name, 'last',inplace=True)
    return dataframe
'''
deletes repeat data values, works with parameters 'dataframe' (set of data you are accessing)
and 'column_name' (name of the column you are acessing), dropping all duplicated values and
printing out the results --> example below
'''
deleteRepeats(ftd, 'FLIGHT_NUMBER')
#deletes repeated flight numbers (in dataframe ftd) to make sure the data isn't skewed by repeats
