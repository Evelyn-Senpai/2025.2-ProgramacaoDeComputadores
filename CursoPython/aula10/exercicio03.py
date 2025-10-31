'''
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.
'''
import random
# while True:
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
valor_jogador = int(input('Diga um valor: '))
par_ou_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
print('-'*20)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor_computador = random.choice(lista)
soma = valor_jogador + valor_computador
print(f'Você jogou {valor_jogador} e o computador {valor_computador}. Total de {soma} DEU ', end='')
print('-'*20)
if soma % 2 == 0:
    print('PAR')
else:
    print('ÍMPAR')
if par_ou_impar in 'Pp':
    print('Você GANHOU!')
    print('-='*20)
else:
    print('Você PERDEU!')
    print('-='*20)