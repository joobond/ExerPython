a,b,s = input().split(" ")
a = int(a)
b = int(b)
s = int(s)

maiorab = ((a+b+abs(a-b)))/2
maioras = ((a+s+abs(a-s)))/2
maior = ((maiorab+maioras+abs(maiorab-maioras)))/2
maior = int(maior)


print(str(maior)+" eh o maior")