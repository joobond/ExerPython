entrada = input().split(" ")
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
lista = [a,b,c]
lista1 = lista.copy()
lista.sort()
for x in range(0,3):
    print("%d"%lista[x])
print("")

for x in range(0,3):
    print("%d" % lista1[x])