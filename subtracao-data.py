from datetime import date

dt_1 = date(2022,5,31)
dt_2 = date(1989,6,12)

#hoje = date.today()
dias = (dt_1 - dt_2).days
anos = dias/365
print(round(anos))
