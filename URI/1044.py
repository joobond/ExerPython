entrada = input().split(" ")
a = int(entrada[0])
b = int(entrada[1])

if((b%a == 0) or (a%b == 0)):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
