#Exercicio 8

import datetime

diaData1=int(input("Digite o dia da primeira data: "))
mesData1=int(input("Digite o mês da primeira data: "))
anoData1=int(input("Digite o ano da primeira data: "))
data1 = datetime.date(day=diaData1, month=mesData1, year=anoData1)
print(data1)
print("---------------------------------------------------")
diaData2=int(input("Digite o dia da segunda data: "))
mesData2=int(input("Digite o mês da segunda data: "))
anoData2=int(input("Digite o ano da segunda data: "))
data2 = datetime.date(day=diaData2, month=mesData2, year=anoData2)
print(data2)
print("----------------------------------------------------")
print("Diferença de dias: ")
diferenca = data2 - data1
print(diferenca.days)