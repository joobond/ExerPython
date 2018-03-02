#Exercicio 9

n = int(input("Digite um número: "))

if n>=1 and n<=10:
    print("Número está entre 1 e 10")
elif n>10 and n<=20:
    print("Número está entre 11 e 20")
elif n<1:
    print("Número inválido!")
else:
    print("Número maior que 20!")
