import numpy as np
import pandas as pd

flights=pd.read_csv('C:\\NSLC\\MajorSim\\atlFlights.csv')
#further cleaning the flights dataset and splitting it into other sets

flights=flights[['MONTH','AIRLINE','ORIGIN_AIRPORT','DESTINATION_AIRPORT','DEPARTURE_TIME','ARRIVAL_TIME','AIR_SYSTEM_DELAY','SECURITY_DELAY']]
#removes extraneous data columns

incomingFlights=flights[flights['DESTINATION_AIRPORT']=='ATL']
incomingFlights=incomingFlights.drop(['DESTINATION_AIRPORT','DEPARTURE_TIME','SECURITY_DELAY',],axis=1)
incomingFlights.to_csv('incomingFlights.csv')
#creates a dataset of all flights arriving at hartsfield jackson,with relevant data

outboundFlights=flights[flights['ORIGIN_AIRPORT']=='ATL']
outboundFlights=outboundFlights.drop(['ORIGIN_AIRPORT','ARRIVAL_TIME','AIR_SYSTEM_DELAY'],axis=1)
outboundFlights.to_csv('outboundFlights.csv')
#creates a dataset of all flights departing from hartsfield jackson,with relevant data

flights.to_csv('atlFlightsUpdate.csv')
#saves the updated data to a single set
