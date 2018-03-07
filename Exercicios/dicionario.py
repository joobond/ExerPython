tabela={
     "alface":2.00,
     "batata":2.50,
     "tomate":3.50,
     "feijão":4.50
 }

print(tabela)

tabela["cebola"]=1.20
del tabela["cebola"]
print(tabela)
print("manga" in tabela)
print("alface" in tabela)
print(tabela.keys())
print(tabela.values())