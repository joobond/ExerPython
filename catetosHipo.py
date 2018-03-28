from math import hypot

op = float(input("Digite o cateto oposto: "))
ad = float(input("Digite o cateto adjacente: "))

h = hypot(op,ad)
print("A hipotenusa é %.2f"%h)