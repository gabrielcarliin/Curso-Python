# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: '))
junto = frase.replace(' ', '').upper()
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(junto, inverso)
if inverso  == junto:
    print('É uma frase palíndroma')
else:
    print('Não é uma frase palíndroma')