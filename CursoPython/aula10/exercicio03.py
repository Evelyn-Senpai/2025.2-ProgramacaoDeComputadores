'''
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.
'''
import random
cont = 0
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
while True:
    valor_jogador = int(input('Diga um valor: '))
    par_ou_impar = ' '
    while par_ou_impar not in 'PI':
        par_ou_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*20)
    valor_computador = random.randint(0, 10)
    soma = valor_jogador + valor_computador
    print(f'Você jogou {valor_jogador} e o computador {valor_computador}. Total de {soma} DEU ', end = '')
    if par_ou_impar == 'P':
        print('PAR')
        print('-'*20)
        if soma % 2 == 0:
            print('Você GANHOU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif par_ou_impar == 'I':
        print('ÍMPAR')
        print('-'*20)
        if soma % 2 == 1:
            print('Você GANHOU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-='*20)
print('-='*20)
print(f'GAME OVER! Você venceu {cont} vezes.')