from math import sqrt
entrada = input().split(" ")
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])
t1 = ((b-c)*1) < a < (b + c)
t2 = ((a-c)*1) <b < (a + c)
t3 = ((a-b)*1) <c < (a + b)

if((t1==True) or (t2==True) or (t3==True)):
    p = a + b + c
    print("Perimetro = %2.1f"%p)
else:
    area = ((a+b)*c)/2
    print("Area = %2.1f"%area)

