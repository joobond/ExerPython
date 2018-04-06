entrada = input().split(" ")
n1 = float(entrada[0])*2
n2 = float(entrada[1])*3
n3 = float(entrada[2])*4
n4 = float(entrada[3])*1
media = (n1+n2+n3+n4)/10
print("Media: %.1f"%media)

if(media>=7.0):
    print("Aluno aprovado.")
elif(media>5.0 and media<=6.9):
    print("Aluno em exame.")
    exame = float(input("Nota do exame: "))
    media = (exame+media)/2
    if(media>=5.0):
        print("Aluno aprovado.")
    elif(media<=4.9):
        print("Aluno reprovado.")
    print("Media final: %.1f"%media)
elif(media<5.0):
    print("Aluno reprovado.")