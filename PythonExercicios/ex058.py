# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.


from random import randint

computador = randint(0, 10)
palpite = 1

print('-+-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-+-' * 20)
print(computador)
jogador = int(input('Digite um número inteiro entre 0 e 10: '))

while computador != jogador:
    palpite += 1
    jogador = int(input('Você errou! Tente novamente: '))

print(f'Depois de {palpite} tentativas, você acertou!')