#Escreva um programa Python para obter uma string feita dos
#primeiros 2 caracteres e dos 2 últimos caracteres de uma string. Se
#o tamanho da string de entrada for menor que 2, retorne uma
#string vazia.
#Exercicio 2
catuaba = "Catuaba"
vodka = "vodka"

if(len(catuaba)<2 and len(vodka)<2):
    str = ""
    print(str)
else:
    str = catuaba[:2]+vodka[3:]
    print(str)