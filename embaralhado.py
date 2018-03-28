import random
def embaralhar(p):
    embaralha = random.sample(p,len(p))
    nova = ''.join(embaralha)
    nova = nova.upper()
    return nova

palavra = input("Digite uma palavra: ")
print(embaralhar(palavra))