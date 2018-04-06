d = int(input())

a = d/365
d_rest = d%365
m = d_rest/30
d_rest = d_rest%30

print(("%d ano(s)\n%d mes(es)\n%d dia(s)")%(a,m,d_rest))