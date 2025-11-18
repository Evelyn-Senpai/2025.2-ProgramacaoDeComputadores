# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número: '))
c = n
f = 1
print('O fatoril de {}! é: '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

# from math import factorial
# n = int(input('Digite um número: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))