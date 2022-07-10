from datetime import datetime

print('================| SISTEMA DE HOTELARIA |================\n\n\n')

tabela_precos = { 'standard' : {'adulto' : 120, 'crianca' : 60},
                  'luxo' : {'adulto' : 180, 'crianca' : 90}
                }

#standard_adultos = tabela_precos.get('standard').get('adulto')
#standard_adulto = tabela_precos['standard']['adulto'] (outra forma de buscar no dicionário)

tipo_hospedagem = input('Tipo hospedagem: (standard) ou (luxo)').lower()
qtd_adultos = int(input('Adultos: '))
qtd_crianca = int(input('Criancas: '))

dt_checkin = datetime.strptime(input('Digite a data de check-in: DD/MM/AAAA'),'%d/%m/%Y').date()
dt_checkout = datetime.strptime(input('Digite a data de check-out: DD/MM/AAAA'),'%d/%m/%Y').date()


qtd_dias_hospedagem = (dt_checkout - dt_checkin).days

valor_frig = float(input('Quanto foi gasto do frigobar:').replace(',','.'))

valortotal_adultos = qtd_adultos * qtd_dias_hospedagem * tabela_precos.get(tipo_hospedagem).get('adulto')
valortotal_crianca = qtd_crianca * qtd_dias_hospedagem * tabela_precos.get(tipo_hospedagem).get('crianca')

valortotal_hospedagempessoas = valortotal_adultos + valortotal_crianca
valor_total = valortotal_hospedagempessoas + valor_frig

print(f'Para a hospedagem {tipo_hospedagem} de {qtd_adultos} adulto(s) e {qtd_crianca} criança(s) para {qtd_dias_hospedagem} dias, o valor ficou em R${valortotal_hospedagempessoas}.\nO gasto do frigobar foi R$ {valor_frig}, deu um total de R${valor_total}')

formade_pagamento = input('Digite a forma de pagamento: [A] à vista ou [P] parcelado').upper()

if formade_pagamento == 'A':
    valordesconto = valor_total * 0.15
    valor_pagamento = valor_total - valordesconto
    
elif formade_pagamento == 'P':
    valor_acrescimo = valor_total * 0.05
    valor_pagamento =  valor_total + valor_acrescimo
    
else:
    valor_pagamento = valor_total
    
print('=================================================================================')

print(f'O total para o pagamento é: R${valor_pagamento}')


