# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

from time import sleep
salario = float(input('Qual o seu salário? '))

if salario > 1250:
    aumento = salario * 1.1
    taxa = 10
if salario < 1250:
    aumento = salario * 1.15
    taxa  =15

print('Calculando...')
sleep(2)

print(f'Salário atual: R$ {salario}')
print(f'Taxa de aumento: {taxa}%')
print(f'Novo salário: R$ {aumento:.2f}')