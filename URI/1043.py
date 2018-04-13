entrada = input().split(" ")
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])
t1 = a < (b + c)
t2 = b < (a + c)
t3 = c < (a + b)

if((t1==True) and (t2==True) and (t3==True)):
    p = a + b + c
    print("Perimetro = %2.1f"%p)
else:
    area = ((a+b)*c)/2
    print("Area = %2.1f"%area)

