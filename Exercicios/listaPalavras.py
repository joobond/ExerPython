#Exercicio 3
estado = True;
lista=[]
while(estado == True):
    palavra = input("Digite uma palavra, se quiser parar, digite 0: ")
    if(palavra == "0"):
        estado = False
        break
    else:
        lista.append(palavra)

if(estado==False):
    maior=max(lista,key=len)
    print(len(maior)," é o tamanho da palavra maior palavra que é",maior)