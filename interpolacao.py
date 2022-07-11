nome = 'Raphael'

print('Olá, ',nome,'seja bem-vindo!')

str_1 = 'Olá, ' +nome+ ' seja bem-vindo!'

print(str_1)

str_2 = 'Olá %s seja bem-vindo!' %nome

print(str_2)

idade = 30

str_3 = 'Olá %s seja bem-vindo! Você tem %d anos.' %(nome,idade)

print(str_3)

str_4  = 'Olá {var_1}, seja bem-vindo, você tem {var_2} anos.' .format(var_1 = nome, var_2 = idade)

print(str_4)

str_5 = f'Olá  {nome}  seja bem-vindo, você tem  {idade} anos.'
print(str_5)
