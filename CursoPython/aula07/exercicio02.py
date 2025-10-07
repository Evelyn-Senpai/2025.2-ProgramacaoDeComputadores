# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para Binário
# - 2 para Octal
# - 3 para Hexadecimal

numero = int(input('Digite um número inteiro qualquer: '))
base = int(input('(1) Binário\n(2) Octal\n(3) Hexadecimal\nEscolha a base de conersão: '))

if base == 1:
    print('{} para Binário é {}'.format(numero,bin(numero)[2:]))
elif base == 2:
    print('{} para Octal é {}'.format(numero,oct(numero)[2:]))
elif base == 3:
    print('{} para Hexadecimal é {}'.format(numero,hex(numero)[2:]))
else:
    print('DIGITE UM VALOR VÁLIDO')