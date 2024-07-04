#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\33[31m', end=' ')
        total += 1
    else:
        print('\033[0;32m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {numero} é divisível {total} vezes')
if total == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')