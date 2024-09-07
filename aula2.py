import pandas as PD
import csv
import seaborn as SNS
import numpy as NP
import statistics as sts
import matplotlib.pyplot as PLT

asyncr = NP.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])

Iris = PD.read_csv('Iris.csv')
#print(Iris.head())
#Dados.['coluna']

Stock = PD.read_csv('stock_data.csv')
#print(Stock.head())

#SNS.boxplot(Stock['Open'])
#PLT.show()

'''''
x = Stock['Open'].mean()
ponto_corte = Stock['Open'].std(ddof=1)*3
inferior, superior = x - ponto_corte, x + ponto_corte
outliers = Stock['Open'][(Stock['Open'] < inferior) | (Stock['Open'] > superior)]
print(outliers)
'''''


x = asyncr.mean()
ponto_corte = asyncr.std(ddof=1)*3
inferior, superior = x - ponto_corte, x + ponto_corte
outliers = asyncr[(asyncr < inferior) | (asyncr > superior)]
print(outliers)