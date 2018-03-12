palavra = input("Digite uma palavra: ")
dicio={}

up = palavra.upper();

if "A" in up:
    dicio['A']=up.count("A")
if "E" in up:
    dicio['E']=up.count("E")
if "I" in up:
    dicio['I']=up.count("I")
if "O" in up:
    dicio['O']=up.count("O")
if "U" in up:
    dicio['U']=up.count("U")

print(dicio)