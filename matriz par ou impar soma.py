matriz = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
somatorio_coluna_0 = 0
somatorio_coluna_1 = 0
somatorio_coluna_2 = 0
    

for indice_linha in range(0,3):
    for indice_coluna in range(0,3):
        print(f'linha: _{indice_linha}_ coluna: |{indice_coluna}| -> {matriz[indice_linha][indice_coluna]}')
        if matriz[indice_linha][indice_coluna]%2 == 0:
            print(f'O valor {matriz[indice_linha][indice_coluna]} é par')
            
        else:
            print(f'o valor {matriz[indice_linha][indice_coluna]} é ímpar')
            
            
        if indice_coluna == 0:
            somatorio_coluna_0 += matriz[indice_linha][indice_coluna]
        elif indice_coluna == 1:
            somatorio_coluna_1 += matriz[indice_linha][indice_coluna]
        elif indice_coluna == 2:
            somatorio_coluna_2 += matriz[indice_linha][indice_coluna]

print(f'A soma da coluna 0 é: {somatorio_coluna_0}')
print(f'A soma da coluna 1 é: {somatorio_coluna_1}')
print(f'A soma da coluna 2 é: {somatorio_coluna_2}')