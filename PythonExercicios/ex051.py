# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

pri_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
dec_termo = pri_termo + (10 - 1) * razao

for c in range(pri_termo, dec_termo + razao, razao):
    print(c, end=' -> ')
print('FIM')