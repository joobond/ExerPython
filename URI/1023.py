consumo = []
cons = []
def main():
    dom = int(input())
    if(dom != 0):
        for i in range(0,dom):
            entrada = input().split(" ")
            x = int(entrada[0])
            y = int(entrada[1])
            cm = int(y/x)
            cons.append(x)
            cons.append(y)
            cons.append(cm)
            consumo.append(cons)
        for i,i2 in consumo:
            print(consumo[i][i2])
    else:
        return False


if __name__=="__main__":
    main()




