#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

num_real = float(input('Digite um número real: '))

print(f'A porção inteira de {num_real} é {math.floor(num_real)}')
print(f'A porção inteira de {num_real} é {int(num_real)}')
print(f'A porção inteira de {num_real} é {math.trunc(num_real)}')