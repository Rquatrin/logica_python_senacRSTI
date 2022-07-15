def entrar_inteiro():
    solicitar_inteiro = True
    while solicitar_inteiro:
        try:
            return int(input('Digite um número inteiro: '))
        
        except:
            
            print('Você deve digitar um número inteiro!')
        
numero = entrar_inteiro()

print(f'O dobro de {numero} é {numero * 2}')