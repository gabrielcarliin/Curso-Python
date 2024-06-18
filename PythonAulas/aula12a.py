# Condições aninhadas

nome = str(input('Qual é seu nome?'))

if nome == 'Gabriel':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Lenita' or nome == 'Filipe':
    print('Seu nome é bem popular no brasil.')
else:
    print('Que nome comum...')
print(f'Tenha um bom dia, {nome}!')