# Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.
import time
from datetime import date

dt_atual = date.today().year
dt_nascto = int(input('Digite o ano de nascimento: '))
idade = dt_atual - dt_nascto

print('Calculando...')
time.sleep(1)

if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = dt_atual + saldo
    print(f'O seu alistamento será em {ano}.')
elif idade == 18:
    print(f'Seja bem vindo ao serviço militar!')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = dt_atual - saldo
    print(f'O seu alistamento foi em {ano}')
