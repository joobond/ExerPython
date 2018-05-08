cont = 0
lista = []
media = 0
for i in range(1,7):
    a = float(input())
    if(a>0):
        cont = cont + 1
        lista.append(a)

for i in lista:
    media = i + media


print("%d valores positivos"%cont)
print("%.1f"%(media/cont))