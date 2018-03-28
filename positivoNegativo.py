def positivoNegativo(a):
    if(a<0 or a==0):
        return "N"
    elif(a>0):
        return "P"

a = int(input("Digite o primeiro argumento: "))
print(positivoNegativo(a))