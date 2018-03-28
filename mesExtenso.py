estado = True
import calendar
months = []
for n in calendar.month_name:
    months.append(n);
def data(d,m,y):
    day = d
    month = m
    year = y

    if(day <= 31):
        monthExt = months[m]
        if(monthExt == 'February' and day > 28 and year%4 == 1):
            print("Fevereiro só tem 28 dias em anos não bissextos")
        elif (monthExt == 'February' and day >=30):
            print("Fevereiro não tem 30 dias nunca!")
        else:
            print(str(day)+" of "+str(monthExt)+" of "+str(year))
    else:
        print("Data inválida!")

while estado == True:
    con = input("Continuar? \n1 para SIM\n2 para NÃO")
    if(con == '1'):
        print("Formato: DD/MM/YYYY")
        day = int(input("Digite o dia: "))
        month = int(input("Digite o mês: "))
        year = int(input("Digite o ano: "))

        data(day,month,year)
        estado == True
    else:
        estado == False