estado = True
def digitos(a):
    if(a != "sair"):
        a = str(a)
        print("O número "+a+" tem "+str(len(a))+" digitos")
        return True
    else:
        return False

while (estado):
    estado = digitos(input("Para sair digite 'sair'\nDigite um número: "))