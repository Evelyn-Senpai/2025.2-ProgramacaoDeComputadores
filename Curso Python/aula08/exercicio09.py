# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

cont_maior = 0
cont_menor = 0
ano_atual = date.today().year

for pessoa in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    
    if (ano_atual - ano) >= 18:
        cont_maior += 1
    else:
        cont_menor += 1

print('\033[32m{} \033[mpessoas já atingiram a maior idade e \033[31m{} \033[mainda não atingiram a maior idade'.format(cont_maior, cont_menor))

