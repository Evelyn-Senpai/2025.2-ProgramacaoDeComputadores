# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se aliste
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))

idade = atual - ano


if idade > 18:
     print('Você tem {} anos, já passou do tempo de se alistar faz {} anos, você deveria ter se alistado em {}'.format(idade,idade-18,ano+18))
elif idade < 18:
    print('Você tem {} anos, vai se alistar daqui a {} anos em {}'.format(idade,18-idade,ano+18))
elif idade == 18:
    print('Você tem {} anos, é hora de se alistar em {}'.format(idade,ano+18))
else:
    print('Digite uma data válida')