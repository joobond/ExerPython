def simplifica(x,y):
    r = x%y
    if(r == 0):
        return y
    else:
        return simplifica(y,r)
def main():
    quantidade = int(input())
    for i in range(0,quantidade):
        split = input()
        split = split.split(" ")
        n1 = int(split[0])
        d1 = int(split[2])
        op = split[3]
        n2 = int(split[4])
        d2 = int(split[6])

        if(op == "+"):
            p1 = int(n1*d2 + n2*d1)
            p2 = int(d1*d2)
            mdc = abs(int(simplifica(max(p1,p2),min(p1,p2))))
            p3 = p1/mdc
            p4 = p2/mdc
            print((("%d/%d = %d/%d")%(p1,p2,p3,p4)))
        elif(op == "-"):
            p1 = int(n1 * d2 - n2 * d1)
            p2 = int(d1 * d2)
            mdc = abs(int(simplifica(max(p1, p2), min(p1, p2))))
            p3 = p1 / mdc
            p4 = p2 / mdc
            print((("%d/%d = %d/%d") % (p1, p2, p3, p4)))
        elif (op == "*"):
            p1 = int(n1 * n2)
            p2 = int(d1 * d2)
            mdc = abs(int(simplifica(max(p1, p2), min(p1, p2))))
            p3 = p1 / mdc
            p4 = p2 / mdc
            print((("%d/%d = %d/%d") % (p1, p2, p3, p4)))
        elif (op == "/"):
            p1 = int(n1 * d2)
            p2 = int(n2 * d1)
            mdc = abs(int(simplifica(max(p1, p2), min(p1, p2))))
            p3 = p1 / mdc
            p4 = p2 / mdc
            print((("%d/%d = %d/%d") % (p1, p2, p3, p4)))
    return

if __name__=="__main__":
    main()