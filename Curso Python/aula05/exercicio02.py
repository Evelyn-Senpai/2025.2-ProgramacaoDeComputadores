# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n1 = int(input('Digite um número entre 0 e 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhares: {}'.format(m))