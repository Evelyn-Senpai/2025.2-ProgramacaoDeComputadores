# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM           - Até 25 anos:SÉNIOR
# - Até 14 anos: INFANTIL       - Acima: MASTER
# - Até 19 anos: JUNIOR

from datetime import date

data = int(input('Ano de nascimento: '))
atual = date.today().year

idade = atual - data

if idade <= 9:
    print('Você tem {} anos, a sua categoria é MIRIM'.format(idade))
elif 9 > idade <= 14:
    print('Você tem {} anos, a sua categoria é INFANTIL'.format(idade))
elif 14 > idade <= 19:
    print('Você tem {} anos, a sua categoria é JUNIOR'.format(idade))
elif 19 > idade <= 25:
    print('Você tem {} anos, a sua categoria é SÉNIOR'.format(idade))
elif idade > 25:
    print('Você tem {} anos, a sua categoria é MASTER'.format(idade))

