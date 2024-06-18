#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite o valor em metro: '))
cm = m * 100
mm = m * 1000

print(f'{m} metros são equivalentes a {cm} centímetros ou {mm} milímetros')