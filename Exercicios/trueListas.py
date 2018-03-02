lista = [6,3,27,82,1]
lista2 = [7,12,67,2,5]

def verfificaLista(lista,lista2):
    for i in lista:
        for j in lista2:
            if i == j:
                return True


if verfificaLista(lista,lista2):
    print("Tem elementos iguais")
else:
    print("Não tem igual")



def verificaListaMaisFacil(lista,lista2):
    listafinal= list(set(lista)+set(lista2))
    print(listafinal)

verificaListaMaisFacil(lista,lista2)

