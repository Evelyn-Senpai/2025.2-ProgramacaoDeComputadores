'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é primo ou não.
'''
import sys
try:
    numero = int(input('Informe um valor inteiro: '))
    if numero < 0:
        sys.exit('ERRO: Informe um valor maior que zero!')
except ValueError:
    sys.exit('ERRO: Informe um valor inteiro!')
except Exception as Erro:
    sys.exit(f'ERRO: {Erro}')
else:
    total = 0
    for contador in range(1, numero+1):
        if numero % contador == 0:
            total +=1
        if total > 2:
            break
    if total == 2:
        print(f'{numero} é primo')
    else:
        print(f'{numero} não é primo')