def soma(L):
    total = 0
    for e in L:
        total += e
    return total

def media(L):
    return  (soma(L) / len(L))

kart={}
campeos={}
tempos = [];
resultados = {};
for c in range(1,7):
    nome = input("Insira o nome do corredor "+str(c)+":")
    for v in range(1,11):
        tempo = float(input("Insira o tempo na volta "+str(v)+":"))
        tempos.append(tempo)

    kart[nome] = tempos
    resultados[nome]=[min(tempos),tempos.index(min(tempos))+1,media(tempos)]
    tempos = []

menorTempo = 0
campeao =""
volta = 0
contador=1
melhor_volta_corredor = ''
melhor_volta_tempo = 0
melhor_volta = 0
for r in resultados.keys():
    tempoAtual=resultados[r][2]
    melhor_volta_atual = resultados[r][0]

    if contador==1:
        menorTempo=tempoAtual
        contador = contador+1
        melhor_volta_tempo = resultados[r][0]
        melhor_volta = resultados[r][1]
    if tempoAtual<=menorTempo:
        menorTempo=tempoAtual
        campeao = r

    if melhor_volta_atual <= melhor_volta_tempo:
        melhor_volta_tempo = melhor_volta_atual
        melhor_volta_corredor = r
        melhor_volta = resultados[r][1]

    campeos[r]=resultados[r][2]

print("-------------------------------------")
print("O campeão é: "+str(campeao))
print("-------------------------------------")
print("A melhor volta foi de "+str(melhor_volta_corredor))
print("Na volta número "+str(melhor_volta))
print("-------------------------------------")
print("-- Classificação --")
cont = 1;
for c in sorted(campeos, key=campeos.get):
    print(str(cont)+"º: "+str(c))
    cont = cont+1



