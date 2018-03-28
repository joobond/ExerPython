from math import factorial
a = [1,2]
b = [4,5,7,8]

n = int(input("Digite um número de 1 à 9: "))

if n in a:
    print(n**3)
elif n%3 == 0:
    print(factorial(n))
elif n in b:
    print("%.2f"%(n/9))