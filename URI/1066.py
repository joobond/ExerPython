positivos = []
negativos = []
pares = []
impares = []
for i in range(1,6):
    a = int(input())
    if(a<0):
        negativos.append(a)
        a = a*-1
    elif(a!=0):
        positivos.append(a)
    if(a%2 == 0 or a ==0):
        pares.append(a)
    else:
        impares.append(a)

print("%d valor(es) par(es)"%len(pares))
print("%d valor(es) impar(es)"%len(impares))
print("%d valor(es) positivo(s)"%len(positivos))
print("%d valor(es) negativo(s)"%len(negativos))