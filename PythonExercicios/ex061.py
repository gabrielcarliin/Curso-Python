# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

pri_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = pri_termo
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1
print('Fim! ')