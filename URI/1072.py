casos = int(input())
cont = 0
a = 0
dentro = []
fora = []
valores = []
while(cont<casos):
    a = int(input())
    valores.append(a)
    cont = cont+1

for j in valores:
    if j >= 10 and j<=20:
        dentro.append(j)
    else:
        fora.append(j)

print("%d in"%len(dentro))
print("%d out"%len(fora))