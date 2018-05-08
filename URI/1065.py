lista = []
for i in range(1,6):
    a = int(input())
    if(a<0):
        a = a*-1
    if(a%2 == 0):
        lista.append(a)
print("%d valores pares"%len(lista))