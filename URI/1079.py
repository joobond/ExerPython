valor = int(input())
list = []

for n in range(1,(valor+1)):
    valor = input().split(" ")
    a = float(valor[0])
    b = float(valor[1])
    c = float(valor[2])
    final = ((a*2)+(b*3)+(c*5))/10
    print("%.1f"%final)


