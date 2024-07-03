# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

nr_tabuada = int(input('Digite um número para gerar a tabuada: '))
multi = 1

print('-=-' * 10)
print(f'Tabuada de {nr_tabuada}'.center(30))
print('-=-' * 10)
for c in range(1, 11):
    multi = c * nr_tabuada
    print(f'{c} x {nr_tabuada} = {multi}')
