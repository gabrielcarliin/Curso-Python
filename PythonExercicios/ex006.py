#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

n1 = int(input('Digite um valor: '))

print(f'O dobro de {n1} é {n1 * 2}')
print(f'O triplo de {n1} é {n1 * 3}')
print((f'A raiz quadrada de {n1} é {math.sqrt(n1):.2f}'))