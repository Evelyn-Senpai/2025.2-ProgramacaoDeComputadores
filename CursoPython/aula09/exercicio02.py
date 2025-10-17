# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

resposta = 0

while resposta != 5:
    v1 = float(input('Digite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))
    print('[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa')
    resposta = int(input('Qual operação você deseja realizar? '))
    if resposta == 1:
        print('A soma entre {} e {} é = {:.1f}'.format(v1,v2, v1+v2))
    elif resposta == 2:
        print('A multiplicação entre {} e {} é = {:.1f}'.format(v1, v2, v1*v2))
    elif resposta == 3:
        if v1 > v2:
            print('O maior entre {} e {} é {}'.format(v1, v2, v1))
        elif v2 > v1:
            print('O maior entre {} e {} é {}'.format(v1, v2, v2))
        else:
            print('{} é igual a {}'.format(v1, v2))

print('FIM')
