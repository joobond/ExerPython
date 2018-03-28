estado = True
def conversao(hora):
    if(hora == "sair"):
        return False
    hora = int(hora)
    if(hora>=12 and hora<=24):
        if(hora == 24):
            print("0 A.M")
            return True
        elif(hora == 12):
            print("12 P.M")
            return True
        else:
            print((str(hora-12)+" P.M."))
            return True
    elif(hora<12 and hora>0):
        print((str(hora)+" A.M"))
        return True
    elif():
        print("Você inseriu um número invalido!\n Número: "+str(hora))
        return True


while(estado):
  estado = conversao(input("Digite 'sair' para parar\nDigite uma hora para conversão: "))
