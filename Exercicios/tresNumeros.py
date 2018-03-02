#Exercicio 10

n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))

soma = n1+n2+n3

if soma/3 == n1:
    print("O triplo da soma é",(soma*3))
else:
    print("A soma é",soma)