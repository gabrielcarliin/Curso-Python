# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Qual a distância da viagem? '))

if distancia <= 200:
    valor = distancia * 0.5
    print('-+-' * 10)
    print(f'Distancia selecionada: {distancia}km')
    print(f'Valor por km: R$ 0,50')
    print(f'Valor total: R$ {valor:.2f}')
    print('-+-' * 10)
else:
    valor = distancia * 0.45
    print('-+-' * 10)
    print(f'Distancia selecionada: {distancia}km')
    print(f'Valor por km: R$ 0,45')
    print(f'Valor total: R$ {valor:.2f}')
    print('-+-' * 10)
