import numpy as NP
import statistics as sts
import matplotlib.pyplot as PLT
import seaborn as SNS

sync = NP.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])

asyncr = NP.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])

barra = '-' * 25
#Média -> dados.mean()
print("MÉDIA")
print(barra)

media1 = sync.mean()
media2 = asyncr.mean()
print("A média de sync é:", media1)
print(barra)
print("A média de asyncr:", media2)
print(barra)

#Mediana -> NP.median(dados)
print("MEDIANA")
print(barra)

me1 = NP.median(sync)
me2 = NP.median(asyncr)
print("A mediana de asyncr:", me1)
print(barra)
print("A mediana de asyncr:", me2)
print(barra)

'''''

Percentil -> Pn = NP.percentile(dados, percentual) -> Pn = NP.percentile(dados, 10)
pn1 = NP.percentile(sync, 10)
print("O primeiro percentil de sync:", pn1)

'''''

#Quartil -> Q1 = NP.percentile(dados, 25)
print("QUARTIL")
print(barra)

q1s = NP.percentile(sync, 25)
q3s = NP.percentile(sync, 75)
print("O primeiro quartil de sync:", q1s)
print(barra)
print("O terceiro quartil de sync:", q3s)
print(barra)

q1a = NP.percentile(asyncr, 25)
q3a = NP.percentile(asyncr, 75)
print("O primeiro quartil de asyncr:", q1a)
print(barra)
print("O terceiro quartil de asyncr:", q3a)
print(barra)

#Moda -> Moda = statistics.multimode(dados)
print("MODA")
print(barra)

moda1 = sts.multimode(sync)
print("A moda de sync:", moda1)
print(barra)

moda2 = sts.multimode(asyncr)
print("A moda de asyncr:", moda2)
print(barra)

#Médidas de dispersão
print("-------MEDIDAS DE DISPERSÃO--------")
print(barra)
#Amplitude -> R = Xmax - Xmin -> max(dados) - min(dados)
print("AMPLITUDE")
print(barra)

#amp1teste= max(sync) - min(sync)
#print("Amplitude:", amp1teste)
amp1 = sync.ptp()
print("Amplitude de sync:", amp1)
print(barra)

amp2 = asyncr.ptp()
print("Amplitude de asyncr:", amp2)
print(barra)

#Amplitude interquartil -> IQR = Q3 - Q1
print("AMPLITUDE INTERQUARTIL")
print(barra)

iqr1teste = q3s - q1s
print("IQR sync:", iqr1teste)

iqr2teste = q3a - q1a
print("IQR asyncr:", iqr2teste)

#Variância -> var = dados.var(ddof=1)
print("Variância")
print(barra)

var1 = sync.var(ddof=1)
print("Variância sync:", var1)
print(barra)

var2 = asyncr.var(ddof=1)
print("Variância asyncr:", var2)
print(barra)

#Desvio padrão
print("Desvio Padrão")
print(barra)

#Desvio padrão da amostra
print("Desvio Padrão da Amostra")
print(barra)

dpa1 = sync.std(ddof=1)
print("Desvio Padrão da Amostra sync:", dpa1)
print(barra)

dpa2 = asyncr.std(ddof=1)
print("Desvio Padrão da Amostra asyncr:", dpa2)
print(barra)

#Desvio padrão da População
print("Desvio Padrão da População")
print(barra)

dpp1 = sync.std(ddof=0)
print("Desvio Padrão da população sync:", dpa1)
print(barra)

dpp2 = asyncr.std(ddof=0)
print("Desvio Padrão da população asyncr:", dpa2)
print(barra)

#Coeficiente de variação
#Apresenta a variabilidade dos dados em percentual
#CV = S / X -> S = Desvio padrão e X = Média
print("Coeficiente de variação")
print(barra)

cv1 = dpa1 / media1
print("Coeficiente de variação sync:", cv1)
print(barra)

cv2 = dpa2 / media2
print("Coeficiente de variação asyncr:", cv2)
print(barra)

#Gráficos
print("-------GRÁFICOS-------")
print(barra)

#Histograma
#Divide a faixa de dados em intervalos, chamados intervalos de classe.
#PLT.hist(dados, bins, range)
#PLT.show()
#bins -> largura do intervalo de classe
#range -> (inicio, final) -> dados.min() e dados.max() -> (min,max) C Range
print("HISTOGRAMA")
print(barra)

min1 = sync.min()
max1 = sync.max()
PLT.hist(sync, 5, (65, 95))
PLT.show()

min2 = asyncr.min()
max2 = asyncr.max()
# Meu range precisa estar dentro de um valor que seja múltiplo do meu bins
PLT.hist(asyncr, 5, (65, 95))
PLT.show()

#Boxplot
# Apresenta o centro, dispersão, desvio da simetria e outliers
print("BOXPLOT")
print(barra)

# SNS.boxplot(dados)
# PLT.show()

SNS.boxplot(sync)
PLT.show()

SNS.boxplot(asyncr)
PLT.show()

# Dispersão
# É analisada nos intervalos entre Min e Q3; Q1 e Me; Me e Q3; Q3 e Max.

SNS.boxplot([sync, asyncr])
PLT.xticks([0, 1], ['Sync', 'Asyncr'])
PLT.xlabel('Work Type')
PLT.ylabel('Hours')
PLT.show()