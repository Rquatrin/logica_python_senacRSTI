from random import randint

n_1 = int(input('Digite o primeiro número do intervalo que deseja sortear:'))

n_2 = int(input('Digite o último número do intervalo que deseja sortear:'))

numero_sorteado = randint(n_1,n_2)
nivel = input('Qual a dificuldade do jogo deseja escolher? [F] para o fácil e [D] para difícil')

if nivel.upper() == 'F':
    qtd_chance = 5

elif nivel.upper() == 'D':
    qtd_chance = 2

else:
    print(f'O nível {nivel} é inválido')
    exit()
    

for chance in range(1,qtd_chance+1):

    numero_digitado = int(input(f'{chance}º chance. Informe um número de 0 a 10: '))

    if numero_sorteado == numero_digitado:
        print(f'Você acertou!Número sorteado foi: {numero_sorteado}')
        exit()
    else:
        if chance == qtd_chance:
            mensagem = 'Inicie novo jogo'
        else:
            mensagem = 'Tente novamente'
        print(f'Você errou!{mensagem}')

print('Você digitou o número: ',numero_digitado,' e o número sorteado foi: ',numero_sorteado)
