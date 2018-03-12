agenda = {}
estado = True

def incluirNome(nome):
    agenda[nome] = []
    print("Novo nome criado\n")

def excluirNome(nome):
    del agenda[nome]
    print("Pessoa excluída com sucesso")

def incluirTel(nome, tel):
    if nome in agenda:
        tels = agenda[nome];
        tels.append(tel);
        agenda[nome] = tels;

        print('Telefone adicionado')
    else:
        add = input("Pessoa nao encontrada. Adicionar? (sim, nao)")
        if add == "sim":
            incluirNome(nome)
            incluirTel(nome, tel)

def excluirTel(nome):
    if nome in agenda:
        tels = agenda[nome]
        count = 1
        if len(tels) < 2:
            c = input("Você excluirá uma pessoa, confirmar? (sim, nao): ")
            if c == 'sim':
                del agenda[nome]
            else:
                return 0;
        else:
            for t in tels:
                print(str(count) +" -> "+ str(t))
                count = count + 1

            numero = int(input("Escolha um telefone da lista: "))
            del tels[numero - 1]

        print("Excluído com sucesso")

def exibirLista():
    print('Adicionar pessoa: (1)')
    print('Adicionar Número: (2)')
    print('Excluir pessoa: (3)')
    print('Excluir número: (4)')
    print('Consultar Lista: (5)')

    return int(input('Escolha uma opção: '))

while estado:
    op = exibirLista()
    if op == 1:
        incluirNome(input("Digite o nome: "))
    elif op == 2:
        incluirTel(input("Digite o nome: "), input("Digite o número"))
    elif op == 3:
        excluirNome(input("Digite o nome: "))
    elif op == 4:
        excluirTel(input("Digite o nome: "))
    elif op == 5:
        for c in agenda:
            print(str(c))
            for t in agenda[c]:
                print(t)
            print("---------------------------")