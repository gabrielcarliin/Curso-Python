# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n3:
    maior = n1
if n2 > n1 and n3:
    maior = n2
if n3 > n2 and n1:
    maior = n3
if n1 < n2 and n3:
    menor = n1
if n2 < n1 and n3:
    menor = n2
if n3 < n2 and n1:
    menor = n3

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')