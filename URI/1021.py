n = float(input())
if(0<=n<=1000000.00):
    cedulas = [100, 50, 20, 10, 5, 2]
    moedas = [100, 50, 25, 10, 5, 1]
    aux = 0
    print("NOTAS:")
    for i in range(0,6):
        aux = n/cedulas[i]
        print(("%d nota(s) de R$ %.2f")%(aux,cedulas[i]))
        n = n%cedulas[i]
    print("MOEDAS:")
    n = n*100
    n = int(n)
    for i in range(0,6):
        aux = round(n/moedas[i],2)
        print(("%d moeda(s) de R$ %.2f") % (aux, moedas[i]/100))
        n = n%moedas[i]