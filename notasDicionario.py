notas={}
estado = True;

while estado == True:
    nome = input("Digite o nome do aluno: ")
    if nome not in notas:
        if (nome != ""):
            n1 = int(input("Digite a primeira nota: "))
            n2 = int(input("Digite a segunda nota: "))
            notas[nome]=[n1,n2]
            print(notas[nome])
        else:
            estado = False
    else:
        media = (notas[nome][0] + notas[nome][1])/2
        print("A média de",nome," é igual: ",media)
