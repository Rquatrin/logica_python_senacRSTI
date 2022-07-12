from datetime import datetime,date

nome = input('Digite seu nome: ')
dt_nascimento = input('Digite a sua data de nascimento: (DD/MM/AAAA)')

dt_nascimento = datetime.strptime(dt_nascimento, '%d/%m/%Y').date()

idade = (date.today() - dt_nascimento).days/365

print(f'{nome} tem {idade} anos')

if idade >=21:
    print(f'{nome} é maior de idade pois tem {idade} anos')

else:
    print(f'{nome} não é maior de idade pois tem {idade} anos')