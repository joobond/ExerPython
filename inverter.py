estado  = True
def inverter(a):
    if(a != "sair"):
        a = str(a)
        print (a[::-1])
        return True
    else:
        return False

while(estado):
    estado = inverter(input("Para sair, digite 'sair'\nDigite um número:"))