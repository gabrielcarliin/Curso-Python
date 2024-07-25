# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
qt_mulher = 0
nm_velho = ''

for c in range(1, 5):
    print(f'=-=-=-= {c} PESSOA =-=-=-=')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo (F/M):')).upper()
    soma_idade += idade
    if c == 1 and sexo == 'M':
        maior_idade_homem = idade
        nm_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nm_velho = nome
    if sexo == 'F' and idade < 20:
        qt_mulher += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nm_velho}')
print(f'Ao todo são {qt_mulher} mulheres com menos de 20 anos')
