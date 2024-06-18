# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vl_casa = float(input('Digite o valor da casa: '))
vl_salario = float(input('Digite seu salário: '))
qt_ano = int(input('Digite em quantos anos será pago: '))

qt_prestacao = qt_ano * 12
vl_prestacao_max = vl_salario * .3
vl_prestacao = vl_casa / qt_prestacao

print(f'Para paga pagar uma casa de R$: {vl_casa:.2f} em {qt_ano} anos', end='')
print(f' a prestação será de R$: {vl_prestacao:.2f}')

if vl_prestacao_max >= vl_prestacao:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo reprovado!')
