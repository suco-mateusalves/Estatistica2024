import pandas as PD
import csv
import seaborn as SNS
import numpy as NP
import statistics as sts
import matplotlib.pyplot as PLT
import matplotlib.dates as mdates


# TIME SERIES
# Análise da variabilidade de determinado dado em função do tempo (eixo x).

Stock = PD.read_csv('stock_data.csv')

Stock['Date'] = PD.to_datetime(Stock['Date'])
#print(Stock.head())

SNS.lineplot(data=Stock, x="Date",y="High")
PLT.show()


