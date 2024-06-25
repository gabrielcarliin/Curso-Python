# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/pix: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

vl_produto = float(input('Digite o valor do produto: '))
print('[1] - à vista dinheiro/pix (10% de desconto)')
print('[2] - à vista no cartão débito (5% de desconto)')
print('[3] - em até 2x no cartão (sem juros)')
print('[4] - 3x ou mais no cartão (20% de juros)')
ie_condicao = int(input('Digite a opção corresponde a condição de pagamento: '))

if ie_condicao == 1:
    vl_pago = vl_produto * 0.9
    print(f'Valor: R$ {vl_pago:.2f}')
elif ie_condicao == 2:
    vl_pago = vl_produto * 0.95
    print(f'Valor: R$ {vl_pago:.2f}')
elif ie_condicao == 3:
    nr_parcela = int(input('Digite o número de parcelas: '))
    if nr_parcela <= 2:
        vl_pago = vl_produto / nr_parcela
        print(f'Valor: {nr_parcela} x {vl_pago:.2f} = R$ {vl_produto:.2f}')
    else:
        print('Número de parcelas inválidas para condição de pagamento')
elif ie_condicao == 4:
    nr_parcela = int(input('Digite o número de parcelas: '))
    if nr_parcela >= 3:
        vl_produto = vl_produto * 1.2
        vl_pago = vl_produto / nr_parcela
        print(f'Valor: {nr_parcela} x {vl_pago:.2f} = R$ {vl_produto:.2f}')
    else:
        print('Número de parcelas inválidas para condição de pagamento')
else:
    print('Opção inválida')
