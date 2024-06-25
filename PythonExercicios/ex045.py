# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
escolha_computador = itens[computador]

print('Suas opções: ')
print('[0] - PEDRA')
print('[1] - PAPEL')
print('[2] - TESOURA')
jogador = int(input('Qual é a sua jogada? '))
escolha_jogador = itens[jogador]

print('-='*15)
print(f'Computador jogou {escolha_computador}')
print(f'Jogador jogou {escolha_jogador}')
print('-='*15)

if computador == 0: # pedra
    if jogador == 0: # pedra
        print('Empate!')
    elif jogador == 1: # papel
        print('Jogador venceu! ')
    elif jogador == 2: # tesoura
        print('Computador venceu! ')
    else:
        print('Jogada inválida!')
elif computador == 1: # papel
    if jogador == 0: # pedra
        print('Computador venceu!')
    elif jogador == 1: # papel
        print('Empate! ')
    elif jogador == 2: # tesoura
        print('Jogador venceu! ')
    else:
        print('Jogada inválida!')
elif computador == 2: # tesoura
    if jogador == 0: # pedra
        print('Jogador venceu!')
    elif jogador == 1: # papel
        print('Jogador perdeu! ')
    elif jogador == 2: # tesoura
        print('Empate! ')
    else:
        print('Jogada inválida!')
