entrada = input().split(" ")
n1 = float(entrada[0])
n2 = float(entrada[1])
n3 = float(entrada[2])
n4 = float(entrada[3])
media = (n1*2+n2*3+n3*4+n4*1)/10
print("Media: %.1f"%media)

if(media>=7.0):
    print("Aluno aprovado.")
elif (media < 5.0):
    print("Aluno reprovado.")
elif(media >= 5.0 and media<7.0):
    print("Aluno em exame.")
    n5 = float(input())
    media = (n5 + media) / 2.0
    print(("Nota do exame: %.1f")%n5)
    if(media>=5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f"%media)
