#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

texto = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(texto)))
print('Só tem espaços? {}' .format(texto.isspace()))
print('É um número? {}' .format(texto.isnumeric()))
print('É alfabético? {}' .format(texto.isalpha()))
print('É alfanumérico? {}' .format(texto.isalnum()))
print('Está em maiúsculas? {}' .format(texto.isupper()))
print('Está em maiúsculas? {}' .format(texto.islower()))
print('Está capitalizida? {}' .format(texto.istitle()))
