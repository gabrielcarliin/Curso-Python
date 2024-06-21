# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

ano_nascto = int(input('Digite o ano de nascimento: '))
dt_atual = date.today().year
nr_idade = dt_atual - ano_nascto

if nr_idade <= 9:
    print(f'Idade: {nr_idade}')
    print(f'Categoria: Mirim ')
elif nr_idade <= 14:
    print(f'Idade: {nr_idade}')
    print('Categoria: Infantil')
elif nr_idade <= 19:
    print(f'Idade: {nr_idade}')
    print('Categoria: Junior')
elif nr_idade <= 25:
    print(f'Idade: {nr_idade}')
    print('Categoria: Sênior')
else:
    print('Categoria: Master')