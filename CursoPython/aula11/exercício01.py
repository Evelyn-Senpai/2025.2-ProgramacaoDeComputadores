'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e móstra-lo por extenso.
'''
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if 0 <= n <= 10:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {contagem[n]}')