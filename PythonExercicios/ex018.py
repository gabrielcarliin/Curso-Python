# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Com o ângulo de {angulo} graus, o valor do seno é de {seno:.2f}, o valor do cosseno é de {cosseno:.2f} e o valor da tangente é de {tangente:.2f}')