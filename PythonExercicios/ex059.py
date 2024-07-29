# Crie um programa que leia dois valores e mostre um menu na tela:

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('[ 1 ] - somar')
    print('[ 2 ] - multiplicar')
    print('[ 3 ] - maior')
    print('[ 4 ] - novos números')
    print('[ 5 ] - sair do programa')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}.')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'O resultado entre {n1} x {n2} é {multiplicacao}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}!')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}!')
        else:
            print('Os dois números são iguais!')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa! ')