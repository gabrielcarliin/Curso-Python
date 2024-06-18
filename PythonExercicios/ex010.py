# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite quantos reais você possui: '))
dolar = 4.99

print(f'Com R$: {real:.2f} você pode comprar {(real / dolar):.2f} dólar!')
