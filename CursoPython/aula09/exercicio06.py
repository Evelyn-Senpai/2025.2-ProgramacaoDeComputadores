'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de um sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
n = int(input('Quantos termos você quer mostrar? '))
f1 = 0
f2 = 1
cont = 3
print('{} -> {} '.format(f1, f2), end='')
while cont <= n:
    f = f1 + f2
    print('-> {} '.format(f), end='')
    f1 = f2
    f2 = f
    cont += 1