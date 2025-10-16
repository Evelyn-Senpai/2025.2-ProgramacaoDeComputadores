# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
peso = 0

for pessoa in range(1, 5+1):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoa)))

    if pessoa == 1:
        maior = peso
        menor = peso
    
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é \033[32m{}kg'.format(maior))
print('\033[mO menor peso é \033[31m{}kg'.format(menor))      