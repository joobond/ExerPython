from math import sqrt
entrada = input().split(" ")
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])
delta = (b**2)-(4*a*c)
if(a != 0 and delta>0):
    r1 = (-b + sqrt(delta))/(2*a)
    print("R1 = %.5f"%r1)
    r2 = (-b - sqrt(delta))/(2*a)
    print("R2 = %.5f"%r2)
else:
    print("Impossivel calcular")