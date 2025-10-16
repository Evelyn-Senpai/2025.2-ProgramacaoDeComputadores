# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

tot_maior = 0
tot_menor = 0
peso = 0

for pessoa in range(1, 5+1):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoa)))

    if peso >= peso:
        tot_maior += 1
    
    else:
        tot_menor += 1

    peso = peso

print(tot_maior, tot_menor)      