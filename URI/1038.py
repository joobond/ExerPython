entrada = input().split(" ")
i = int(entrada[0])
q = int(entrada[1])

lista = { 1:4.00,
          2:4.50,
          3:5.00,
          4:2.00,
          5:1.50}

valor = lista[i]
valor = valor*q

print("Total: R$ %.2f"%valor)