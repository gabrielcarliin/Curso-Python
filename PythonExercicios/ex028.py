# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

computador = random.randint(0, 5) # Faz o computador "PENSAR"
print('-+-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-+-' * 20)
jogador = int(input('Digite um número inteiro entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)

if computador == jogador:
    print('YOU WIN! :)')
else:
    print('YOU LOSE! :(')
