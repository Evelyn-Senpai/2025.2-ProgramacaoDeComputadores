# Crie um programa que leia um número qualquer pelo teclado e mostre na tela sua porção inteira. 
# Ex:
# Digite um número qualquer: 6.127
# O número 6.127 tem a parte interira 6.
from math import trunc
n1 = float(input('Digite qualquer número: '))
print('O número {} tem a parte inteira {}'.format(n1, trunc(n1)))

# Faça um programa que lia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retãngulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
calc = hypot(catop, catadj)
print('O comprimento da hipotenusa é: {:.2f}'.format(calc))

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ãngulo.
import math
ang = int(input('Digite o valor do ãngulo: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo {}° tem\nSENO = {:.2f}\nCOSSENO = {:.2f}\nTANGENTE = {:.2f}'.format(ang, seno, coss, tang))

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundp aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))

# Faça uma lista que leia os valores em ordem aleatória.
import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundp aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem será:')
print(lista)
