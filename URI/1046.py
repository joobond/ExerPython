entrada = input().split(" ")
a = int(entrada[0])
b = int(entrada[1])

if(a>b):
    h = (24-a)+b
    print("O JOGO DUROU %d HORA(S)" % h)
elif(b>a):
    h = b-a
    print("O JOGO DUROU %d HORA(S)" % h)
elif(a==b):
    h = 24
    print("O JOGO DUROU %d HORA(S)" % h)

