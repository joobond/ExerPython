while True:
    tabuada = int(input("Qual é a tabuada que você quer?"))

    x = 1
    while x<=10:
        resultado=tabuada*x
        print(x,"x",tabuada,"=",resultado)
        x=x+1
