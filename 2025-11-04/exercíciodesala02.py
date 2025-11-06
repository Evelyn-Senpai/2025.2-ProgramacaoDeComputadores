'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é um número triangular ou não.

   Um número triangular é um número que pode ser representado na forma 
   de um triângulo equilátero.

   Os primeiros números triangulares são: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
'''
from random import triangular
import sys
try:
    numero = int(input('Informe um valor inteiro: '))
    if numero < 0:
        sys.exit('ERRO: O valor informado deve ser maior que 0!')
except ValueError:
    sys.exit('ERRO: O valor informado deve ser inteiro!')
except KeyboardInterrupt:
    sys.exit('ERRO: Ctrl + C pressionado')
except Exception as Erro:
    sys.exit(f'ERRO: {Erro}')
else:
    if numero < 1:
        sys.exit(f'{numero} não é triangular')
    triangular = 0
    incremento = 1
    while triangular < numero:
        triangular += incremento
        incremento += 1
    if triangular == numero:
        print(f'\033[0;32mnúmero {numero} é triangular')
    else:
        print(f'\033[0;31mO número {numero} não é triangular')