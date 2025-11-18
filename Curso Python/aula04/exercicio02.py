# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retãngulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
calc = hypot(catop, catadj)
print('O comprimento da hipotenusa é: {:.2f}'.format(calc))