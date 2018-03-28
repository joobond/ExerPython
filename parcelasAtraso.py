estado = True
lista = []
def valorPagamento(valor,atraso):
    if(valor !=0):
        if(atraso == 0):
            lista.append(valor)
            return True
        else:
            valor = (valor*1.03)+(valor*0.001)
            lista.append(valor)
            return True
    else:
        print("Valor Pago: R$" + str(sum(lista)))
        print("Quantidade de valores pagos: " + str(len(lista)))
        return False

while(estado):
    valor = float(input("Digite o valor a ser pago: "))
    if(valor != 0):
        atraso = int(input("Digite a quantidade de dias em atraso: "))
    estado = valorPagamento(valor,atraso)