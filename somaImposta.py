def somaImposto(imposto,valor):
    imposto = (imposto/100)+1
    return imposto*valor

imposto = float(input("Digite o valor do imposto: "))
valor = float(input("Digite o valor do produto: "))
print(somaImposto(imposto,valor))