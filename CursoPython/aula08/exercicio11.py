# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho.
# = Quantas mulheres têm menos de 20 anos.

cont_media = 0
idade = 0

for pessoa in range(1, 5):
    nome = str(input('Qual o nome da {}ª pessoa? '.format(pessoa)))
    idade = int(input('Qual a idade da {}ª pessoa? '.format(pessoa)))
    sexo = bool(input('Qual o sexo da {}ª pessoa? (F) (M): '.format(pessoa)))

    idade += idade

print('A média das idades é: {}'.format(idade/4))