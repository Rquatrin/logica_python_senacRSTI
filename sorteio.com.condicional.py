from random import randint

numero_sorteado = randint(0,10)

for chance in range(1,4):

    numero_digitado = int(input(f'{chance}º chance. Informe um número de 0 a 10: '))

    if numero_sorteado == numero_digitado:
        print(f'Você acertou!Número sorteado foi: {numero_sorteado}')
        exit()
    else:
        if chance == 3:
            mensagem = 'Inicie novo jogo'
        else:
            mensagem = 'Tente novamente'
        print(f'Você errou!{mensagem}')
    

print('Você digitou o número: ',numero_digitado,' e o número sorteado foi: ',numero_sorteado)
