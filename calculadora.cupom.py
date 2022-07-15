
cupom = input('Digite o código do seu cupom: ')
cupom = cupom.upper()
valortotal_compra = 100.00
if cupom == 'CUPOM10':
    valor_desconto = valortotal_compra * 0.1
    valortotalcompra_desconto = valortotal_compra - valor_desconto
    print('O valor total com seu cupom de desconto de 10% é: R$',valortotalcompra_desconto)

elif cupom == 'CUPOM25':
    valor_desconto = valortotal_compra * 0.25
    valortotalcompra_desconto = valortotal_compra - valor_desconto
    print('O valor total com seu cumpom de desconto de 25% é: R$',valortotalcompra_desconto)
    
elif cupom == 'CUPOM50':
    valor_desconto = valortotal_compra * 0.5
    valortotalcompra_desconto = valortotal_compra - valor_desconto
    print('O valor total com seu cumpom de desconto de 50% é: R$',valortotalcompra_desconto)
    
else:
    print('Você não adicionou um cupom. O valor total é: R$',valortotal_compra)
