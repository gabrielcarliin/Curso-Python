#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor original do produto: '))
desconto = int(input('Digite o valor do desconto em %: '))

valordesconto = preco * ((100-desconto)/100)

print(f'O produto que custava R$ {preco:.2f}, na promoção com desconto de {desconto}% vai custar R$: {valordesconto:.2f}')