import pandas as PD
import csv
import seaborn as SNS
import numpy as NP
import statistics as sts
import matplotlib.pyplot as PLT
import matplotlib.dates as mdates
import scipy.stats


# TIME SERIES
# Análise da variabilidade de determinado dado em função do tempo (eixo x).

Iris = PD.read_csv('Iris.csv')
Stock = PD.read_csv('stock_data.csv')

'''''
Stock['Date'] = PD.to_datetime(Stock['Date'])
#print(Stock.head())

SNS.lineplot(data=Stock, x="Date",y="Open")
SNS.lineplot(data=Stock, x="Date",y="Close")
#SNS.lineplot(data=Stock, x="Date",y="High")
PLT.show()
'''''

# Gráfico de dispersão
# Representa a relação entre duas variáveis.

variavel1 = Iris['SepalLengthCm']
variavel2 = Iris['SepalWidthCm']
#scipy.stats.spearmanr(variavel1, variavel2)
#scipy.stats.pearsonr(variavel1, variavel2)
SNS.scatterplot(data=Iris, x='SepalLengthCm', y='SepalWidthCm')
PLT.show()

SNS.boxplot([variavel1, variavel2])
PLT.xticks([0, 1], ['SepalLengthCm', 'SepalWidthCm'])
PLT.show()

