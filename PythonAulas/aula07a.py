n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}'.format(n1+n2))
print('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' ')
print('Divisão inteira {} e a potência {}'. format(di, e))