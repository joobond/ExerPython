entrada = input().split(" ")
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])
arestas = [a,b,c]
arestas.sort(reverse=True)
a = arestas[0]
b = arestas[1]
c = arestas[2]

a2 = a**2
b2 = b**2
c2 = c**2
if(a>=b+c):
    print("NAO FORMA TRIANGULO")
elif(a2 == b2+c2):
    print("TRIANGULO RETANGULO")
elif(a2>b2+c2):
    print("TRIANGULO OBTUSANGULO")
elif(a2<b2+c2):
    print("TRIANGULO ACUTANGULO")
if(a==b==c):
    print("TRIANGULO EQUILATERO")
elif(a==b or b==c or a==c):
    print("TRIANGULO ISOSCELES")





