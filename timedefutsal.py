time_a = []
time_b = [] 
#guardar nome e numero de camiseta

for i in range(1,11):
    nome = input('Nome: ')
    nr_camisa = int(input('Número da camisa: '))
    
    if len(time_a) < 5:
        time_a.append({'Nome: ' : nome , 'Número da camisa: ' : nr_camisa})
    
    elif len(time_b) < 5:
        time_b.append({'Nome: ' : nome , 'Número da camisa: ' : nr_camisa})
        
print('Jogadores do time A:')
for jogador in time_a:
    print(jogador.get('Número da camisa: ') , jogador.get('Nome: '))
print('Jogadores do time B')
for jogador in time_b:
    print(jogador.get('Número da camisa: ') , jogador.get('Nome: '))


    