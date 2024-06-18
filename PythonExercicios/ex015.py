#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Quantos km foram percorridos? '))
dia = int(input('Quantos dias foram alugadas? '))
valor = (km * 0.15) + (dia * 60)

print(f'O valor total a pagar é de R$ {valor:.2f}')
