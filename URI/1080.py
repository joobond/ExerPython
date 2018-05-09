controle = 0
indice = 0
for n in range(1,101):
    valor = int(input())
    if(valor>controle):
        controle = valor
        indice = n

print(controle)
print(indice)