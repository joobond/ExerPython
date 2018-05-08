list = []

valor = int(input())


if(valor%2 == 1):
    list.append(valor)
    while(len(list)<6):
        ultimo = list[len(list) - 1]
        a = ultimo + 2
        if(a%2 == 1):
            list.append(a)
else:
    valor = valor+1
    list.append(valor)
    while (len(list) < 6):
        ultimo = list[len(list) - 1]
        a = ultimo + 2
        if (a % 2 == 1):
            list.append(a)


for i in range(0,6):
    print(list[i])