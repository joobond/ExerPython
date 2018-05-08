import calendar
m = int(input())

meses = []

for name in calendar.month_name:
    meses.append(name)

print(meses[m])