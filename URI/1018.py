n = int(input())
if(0<n<1000000):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    aux = 0
    print("%d"%n)
    for i in range(0,7):
        aux = n/cedulas[i]
        print(("%d nota(s) de R$ %d,00")%(aux,cedulas[i]))
        n = n%cedulas[i]

