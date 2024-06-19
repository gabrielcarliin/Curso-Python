# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nr_nota1 = float(input('Digite a primeira nota: '))
nr_nota2 = float(input('Digite a segunda nota: '))
nr_media = (nr_nota1 + nr_nota2) / 2

if nr_media < 5:
    print('=' * 25)
    print(f'Média: {nr_media}')
    print(f'Você está reprovado!')
    print('=' * 25)
elif 5 < nr_media < 7:
    print('=' * 25)
    print(f'Média: {nr_media}')
    print('Você está de recuperação!')
else:
    print('=' * 25)
    print(f'Média: {nr_media}')
    print('Você está aprovado!')
