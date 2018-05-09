def par(v):
    v = int(v)
    if(v % 2 == 0):
        return True
    else:
        return False
def positivo(v):
    v = int(v)
    if(v < 0):
        return False
    else:
        return True

valor = int(input())
list = []

for n in range(1,(valor+1)):
    valor = int(input())
    list.append(valor)


for i in list:
    if(i == 0):
        print("NULL")
    elif(par(i) == True):
        if(positivo(i) == True):
            print ("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if (positivo(i) == True):
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
