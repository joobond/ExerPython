entrada = input().split(" ")
x = round(float(entrada[0]),1)
y = round(float(entrada[1]),1)

if(x == y == 0.0):
    print("Origem")
elif(x>0) and (y>0):
    print("Q1")
elif(x>0) and (y<0):
    print("Q4")
elif(x<0) and (y<0):
    print("Q3")
elif(x<0) and (y>0):
    print("Q2")
elif(y==0):
    print("Eixo X")
elif(x==0):
    print("Eixo Y")