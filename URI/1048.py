s = float(input())

if(s>0 and s<=400.00):
    i = 15
    r = float(s*(i/100))
    s = s+r
    print(("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %").format(s,r,i))
elif(s>400.00 and s<=800.00):
    i = 12
    r = float(s*(i/100))
    s = s+r
    print(("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %").format(s,r,i))
elif(s>800.00 and s<=1200.00):
    i = 10
    r = float(s*(i/100))
    s = s+r
    print(("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %").format(s,r,i))
elif(s>1200.00 and s<=2000.00):
    i = 7
    r = float(s*(i/100))
    s = s+r
    print(("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %").format(s,r,i))
elif(s>2000.00):
    i = 4
    r = float(s*(i/100))
    s = s+r
    print(("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %").format(s,r,i))
