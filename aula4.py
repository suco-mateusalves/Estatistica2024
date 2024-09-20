import pandas as PD
import csv
import seaborn as SNS
import numpy as NP
import statistics as sts
import matplotlib.pyplot as PLT
import matplotlib.dates as mdates
import scipy.stats
import scipy

sync = NP.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])

asyncr = NP.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])

Iris = PD.read_csv('Iris.csv')

Stock = PD.read_csv('stock_data.csv')

'''''
Inferência Estatística

Teste de Hipótese

1) Teste de normalidade (Shapiro-Wilk)

H0 é a hipótese NULA
H0: é que a distribuição é normal

H1 é a hipótese alternativa.
H1: é que a distribuição não é normal

Resultado do teste é o P-valor
Atribuir um intervalo de confiança. 
-> Default é 95%
-> 5% erro
-> Limite do P-valor = 0,05

Se P-valor for menor que o limite (0,05), então a hipótese NULA é rejeitada.
                                                                E ASSUMO H1!!!

Se P-valor for maior que o limite (0,05), então a hipótese nula não pode ser rejeitada!
-> P = 0,01
-> P = 0,07

-------------------------

Considere H1:
Assimetria
scipy.stats.skew(dados)
~= 0 simétrica
> 0 cauda a direita
< 0 cauda a esquerda

Considere H0:
Curtose
scipy.stats.kurtosis(dados)
> 0
= 0
< 0
'''''
def hipotese (p):
    if p < 0.05:
        print("Rejeite H0")
    else:
        print("Não Rejeite H0")

s1, p1 = scipy.stats.shapiro(sync)
hipotese(p1)
s2, p2 = scipy.stats.shapiro(asyncr)
hipotese(p2)

print(scipy.stats.skew(sync))
print(scipy.stats.skew(asyncr))

print(scipy.stats.kurtosis(sync))
print(scipy.stats.kurtosis(asyncr))
