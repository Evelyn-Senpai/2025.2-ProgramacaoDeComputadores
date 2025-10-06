# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ãngulo.
import math
ang = int(input('Digite o valor do ãngulo: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo {}° tem\nSENO = {:.2f}\nCOSSENO = {:.2f}\nTANGENTE = {:.2f}'.format(ang, seno, coss, tang))