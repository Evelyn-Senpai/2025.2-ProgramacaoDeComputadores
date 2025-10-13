# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: ABAIXO DO PESO
# - Entre 18.5 e 25: PESO IDEAL
# - 25 até 30: SOBREPESO
# - 30 até 40: OBESIDADE
# - Acima de 40: OBESIDADE MÓRBIDA

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))

imc = peso/altura**2

print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está SOBREPESO')
elif 30 <= imc < 40:
    print('Você está OBESO')
else:
    print( 'Você está com OBESIDADE MÓRBIDA')