# Crie um programa que leia um número qualquer pelo teclado e mostre na tela sua porção inteira. 
# Ex:
# Digite um número qualquer: 6.127
# O número 6.127 tem a parte interira 6.
from math import trunc
n1 = float(input('Digite qualquer número: '))
print('O número {} tem a parte inteira {}'.format(n1, trunc(n1)))