# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho.
# = Quantas mulheres têm menos de 20 anos.

cont_idade = 0
cont_media = 0
cont_idade_maior_h = 0
nome_maior_h = ''
cont_idade_f = 0

for pessoa in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = str(input('Qual o nome da {}ª pessoa? '.format(pessoa))).strip()
    idade = int(input('Qual a idade da {}ª pessoa? '.format(pessoa)))
    sexo = str(input('Qual o sexo da {}ª pessoa? (F) (M): '.format(pessoa))).strip()

    cont_idade += idade
    cont_media += 1

    if pessoa == 1 and sexo in 'Mm':
        cont_idade_maior_h = idade
        nome_maior_h = nome
    if sexo in 'Mm' and idade > cont_idade_maior_h:
        cont_idade_maior_h = idade
        nome_maior_h = nome
    
    elif sexo in 'Ff' and idade < 20:
        cont_idade_f += 1

print('A média das idades é: {:.1f}'.format(cont_idade/cont_media))
print('O homem mais velho é: {}'.format(nome_maior_h))
print('Tem {} mulheres com menos de 20 anos'.format(cont_idade_f))