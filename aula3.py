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

#Species
irissetosa = Iris[Iris['Species']=='Iris-setosa'] 
irisversicolor = Iris[Iris['Species']=='Iris-versicolor']
irisvirginica = Iris[Iris['Species']=='Iris-virginica']
'''''
#Iris Setosa
SNS.scatterplot(data=irissetosa, x='SepalLengthCm', y='SepalWidthCm')
PLT.title("Setosa: SepalLengthCm vs SepalWidthCm")
PLT.show()
SNS.scatterplot(data=irissetosa, x='SepalLengthCm', y='PetalLengthCm')
PLT.title("Setosa: SepalLengthCm vs PetalLengthCm")
PLT.show()
SNS.scatterplot(data=irissetosa, x='PetalLengthCm', y='PetalWidthCm')
PLT.title("Setosa: PetalLengthCm vs PetalWidthCm")
PLT.show()
SNS.scatterplot(data=irissetosa, x='SepalWidthCm', y='PetalWidthCm')
PLT.title("Setosa: SepalWidthCm vs PetalWidthCm")
PLT.show()

#Iris Versicolor
SNS.scatterplot(data=irisversicolor, x='SepalLengthCm', y='SepalWidthCm')
PLT.title("SepalLengthCm vs SepalWidthCm")
PLT.show()
SNS.scatterplot(data=irisversicolor, x='SepalLengthCm', y='PetalLengthCm')
PLT.title("SepalLengthCm vs PetalLengthCm")
PLT.show()
SNS.scatterplot(data=irisversicolor, x='PetalLengthCm', y='PetalWidthCm')
PLT.title("PetalLengthCm vs PetalWidthCm")
PLT.show()
SNS.scatterplot(data=irisversicolor, x='SepalWidthCm', y='PetalWidthCm')
PLT.title("SepalWidthCm vs PetalWidthCm")
PLT.show()

#Iris Virginica
SNS.scatterplot(data=irisvirginica, x='SepalLengthCm', y='SepalWidthCm')
PLT.show()
SNS.scatterplot(data=irisvirginica, x='SepalLengthCm', y='PetalLengthCm')
PLT.show()
SNS.scatterplot(data=irisvirginica, x='PetalLengthCm', y='PetalWidthCm')
PLT.show()
SNS.scatterplot(data=irisvirginica, x='SepalWidthCm', y='PetalWidthCm')
PLT.show()
'''''
irissetosa_drop = irissetosa.drop(columns=['Id','Species'])
#print(irissetosa_drop.head())

corrmatrix_irissetosa_drop = irissetosa_drop.corr()
print(corrmatrix_irissetosa_drop)
SNS.heatmap(corrmatrix_irissetosa_drop, annot=True)
PLT.show()