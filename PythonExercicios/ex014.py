#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

celsius = float(input('Digite a tempetura em celsius: '))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} graus celsius equivale a {fahrenheit} graus fahrenheit")
