#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário atual? R$: '))
aumento = int(input('Em quantos % será o aumento? '))
novosalario = ((100 + aumento) / 100) * salario

print(f'O salário de R$ {salario:.2f} com o aumento de {aumento}% ficará no valor de R$: {novosalario:.2f}')