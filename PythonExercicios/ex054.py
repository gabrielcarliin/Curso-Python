# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year

maior_idade = 0
menor_idade = 0
for c in range(1, 8):
    ano_nascto = int(input(f'Ano de nascimento pessoa {c}: '))
    idade = ano_atual - ano_nascto
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'Ao todo são {maior_idade} pessoas maiores de idade')
print(f'Ao todo são {menor_idade} pessoas menores de idade')
