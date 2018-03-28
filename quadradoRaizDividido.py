from math import sqrt
a = [1,2,3]
b = [4,9]
c = [6,7,8]

n = int(input("Digite um número de 1 à 9: "))

if n in a:
    print(n**2)
elif n in b:
    print(sqrt(n))
elif n in c:
    print("%.2f"%(n/9))

