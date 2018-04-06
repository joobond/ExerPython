a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

atr = (a*c)/2
ac = c**2*(3.14159)
at = (c*(a+b))/2
aq = b**2
ar = a*b

print(("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f")%
      (atr,ac,at,aq,ar))