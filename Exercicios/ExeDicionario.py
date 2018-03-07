estado = True
tabela={
     "alface":2.00,
     "batata":2.50,
     "tomate":3.50,
     "feijão":4.50
 }

while(estado == True):
    palavra = input("Qual produto você deseja? Digite 'fim' para sair")
    if(palavra != "fim"):
        if(palavra in tabela):
            print(palavra,tabela[palavra])
            delete = input("Deseja deletar?")
            if(delete == "sim" or delete=="Sim"):
                del tabela[palavra]
                print("Produto deletado")
            else:
                print("Ok")
        else:
            conf=input("Produto não encontrado, deseja incluir?")
            if(conf == "sim" or conf=="Sim"):
                valor = float(input("Digite o valor: "))
                tabela[palavra]=valor
                print("Produto incluído")
            else:
                print("Ok")
    else:
        estado = False
        print("Fim da consulta")
        break;