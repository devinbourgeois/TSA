import numpy as np
import pandas as pd

flightsData=pd.read_csv('C:\\NSLC\\MajorSim\\flights.csv')
#reads the data
flightsData=flightsData[flightsData['Z']==True]
#sorts for only rows with value 'Z' in it (indicating whether or not the flight came from or left from ATL)
flightsData.to_csv('atlFlights.csv')

