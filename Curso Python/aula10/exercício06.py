'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas células de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, 20, 10 e 1.
'''
print('='*40)
print('BANCO EV'.center(40))
print('='*40)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50
total_cedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if total == 0:
            break
print('='*40)
print('Volte sempre ao BANCO EV! Tenha um bom dia!')