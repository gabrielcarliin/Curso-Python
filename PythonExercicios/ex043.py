# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

qt_peso = float(input('Digite seu peso: '))
qt_altura = float(input('Digite sua altura em cm: '))
imc = qt_peso / ((qt_altura/100)**2)

print(f'Seu imc é {imc:.2f}')

if imc < 18.5:
    print('Status: Abaixo do peso')
elif imc < 25:
    print('Status: Peso Ideal')
elif imc < 30:
    print('Status: Sobrepeso')
elif imc < 40:
    print('Status: Obesidade')
else:
    print('Status: Obesidade Mórbida')