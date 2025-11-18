# Faça um programa que faça o computador jogar Pedra, Papel e Tesoura com você

import random

print('SUAS OPÇÕES:\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura')
opcao = int(input('Qual a sua jogada? '))
print('PEDRA!\nPAPEL!!\nTESOURA!!!')

lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = random.choice(lista)

if opcao == 1:
    print('O jogador jogou PEDRA')
    print('O computador jogou {}'.format(escolha))
    if escolha == 'PEDRA':
        print('EMPATE')
    elif escolha == 'PAPEL':
        print('COMPUTADOR GANHOU')
    elif escolha == 'TESOURA': 
        print('JOGADOR GANHOU')
    else:
        print('Jogada Inválida')
elif opcao == 2:
    print('O jogador jogou PAPEL')
    print('O computador jogou {}'.format(escolha))
    if escolha == 'PAPEL':
        print('EMPATE')
    elif escolha == 'TESOURA':
        print('COMPUTADOR GANHOU')
    elif escolha == 'PEDRA  ': 
        print('JOGADOR GANHOU')
    else:
        print('Jogada Inválida')
else:
    print('O jogador jogou TESOURA')
    print('O computador jogou {}'.format(escolha))    
    if escolha == 'TESOURA':
        print('EMPATE')
    elif escolha == 'PAPEL':
        print('JOGADOR GANHOU')
    elif escolha == 'PEDRA': 
        print('COMPUTADOR GANHOU')
    else:
        print('Jogada Inválida')