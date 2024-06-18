#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura em metros: '))
altura = float (input('Digite a altura em metros: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e a sua área é de {area}m2.')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')