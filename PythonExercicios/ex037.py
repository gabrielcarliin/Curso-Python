# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

nr_inteiro = int(input('Digite um número inteiro: '))
print('Opções de conversão: \n1 - Binário\n2 - Octal\n3 - Hexadecimal')
ie_base_conversao = int(input('Digite a opção desejada: '))

binario = bin(nr_inteiro)
octal = oct(nr_inteiro)
hexadecimal = hex(nr_inteiro)

if ie_base_conversao == 1:
    print(f'O número {nr_inteiro} convertido em binário é: {binario}')
elif ie_base_conversao == 2:
    print(f'O número {nr_inteiro} convertido em octal é: {octal}')
elif ie_base_conversao == 3:
    print(f'O número {nr_inteiro} convertido em hexadecimal é: {hexadecimal}')
else:
    print('Opção inválida, tente novamente!')