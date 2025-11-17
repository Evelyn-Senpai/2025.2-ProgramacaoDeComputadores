'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
soma = maior = menor = cont= 0
opcao = 'S'
while opcao not in 'Nn':
    n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma/cont
print('A média dos {} números é {:.2f}'.format(cont, media))
print('O maior deles é {} e o menor é {}'.format(maior, menor))