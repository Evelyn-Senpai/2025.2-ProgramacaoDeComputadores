'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas células de cada valor serão entregues.
OBS: Considere que o caixa possui células de R$ 50, 20, 10 e 1.
'''
print('='*40)
print('BANCO EV')
print('='*40)
valor = int(input('Que valor você quer sacar? R$ '))
c_50 = c_20 = c_10 = c_1 = 0
while valor >= 0:
    if valor % 50 == 0:
        c_50 += 1
    elif valor % 20 == 0:
        c_20 += 1
    elif valor % 10 == 0:
        c_10 += 1
    else:
        c_1 += 1
print(f'Total de {c_50} céculas de R$ 50')
print(f'Total de {c_20} céculas de R$ 20')
print(f'Total de {c_10} céculas de R$ 10')
print(f'Total de {c_1} céculas de R$ 1')
print('='*40)
print('Volte sempre ao BANCO EV! Tenha um bom dia!')