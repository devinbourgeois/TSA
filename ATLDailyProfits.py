import numpy as np
import pandas as pd

daily_profit = pd.read_excel('ATL_Daily_Profit.xlsx')
#reads the data

daily_profit.drop('INBOUND FLIGHTS',inplace=True,axis=1)
daily_profit.drop('OUTBOUND FLIGHTS',inplace=True,axis=1)
#drops the inbound and outbound flight columns

daily_profit.loc[[272,273,274,275,276,277,278,279,280]]
daily_profit.loc[[272,291,292,293,294,295,296,297,298,299,300,301,302,303,304]]
#locates null values

daily_profit.drop([291,292,293,294,295,296,297,298,299,300,301,302,303],inplace=True,axis=0)
daily_profit.drop([273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290], inplace=True,axis=0)
#deletes null values

daily_profit.reset_index(inplace=True)
#resetting index numbers

daily_profit.to_csv("CleanedATLProfits1.csv")
#saving cleaned profits to .csv
