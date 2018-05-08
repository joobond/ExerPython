s = float(input())

if(s>0 and s<=2000.00):
    print("Isento")
elif(s>2000.00 and s<=3000.00):
    t = (s - 2000)
    tx = (t * 8) / 100
    print("R$ %.2f" % tx)
elif(s>3000.00 and s<=4500.00):
    t = (s - 2000)
    t1 = t - 1000
    tx1 = (1000 * 8) / 100
    tx2 = (t1 * 18) / 100
    print("R$ %.2f" % (tx1 + tx2))
elif(s>4500.00):
    t = (s - 2000)
    t1 = t - 1000
    tx1 = (1000 * 8) / 100
    t2 = t1 - 1500
    tx2 = (1500 * 18) / 100
    tx = (t2 * 28) / 100
    print("R$ %.2f" % (tx + tx1 + tx2))
