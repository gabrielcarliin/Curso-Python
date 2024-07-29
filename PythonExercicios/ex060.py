# Faça um programa que leia um número qualquer e mostre o seu fatorial.

n1 = int(input('Digite um número inteiro para calcular seu fatorial: '))
c = n1
f = 1
print(f'Calculando {n1}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)