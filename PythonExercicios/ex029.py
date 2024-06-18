# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Digite a velocidade do carro: '))
valor_multa = (velocidade - 80) * 7

if velocidade > 80:
    print('MULTADO! O carro excedeu o limite de 80km/h! ')
    print(f'Valor da multa: R$ {valor_multa:.2f}')
else:
    print('Bom dia! Dirija com segurança! :)')
