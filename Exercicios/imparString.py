#Exercicio 4
palavra = input("Digite a palavra: ")
palavraFormatada = ""

for i, x in enumerate(palavra):
    if(i%2 ==0):
        palavraFormatada+=x

print(palavraFormatada)
