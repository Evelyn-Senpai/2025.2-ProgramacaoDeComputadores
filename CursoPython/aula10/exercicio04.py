'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
'''
cont_18_idade = cont_20_mulheres = homens = 0
print('='*20, 'FRIM DO PROGRAMA', '='*20)
while True:
    print('-'*40)
    print('CADASTRE UMA PESSOA')
    print('-'*40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        cont_18_idade += 1
    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            cont_20_mulheres += 1
    print('-'*40)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('='*20, 'FRIM DO PROGRAMA', '='*20)
print(f'Total de pessoas com mais de 18 anos: {cont_18_idade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {cont_20_mulheres} mulheres com menos de 20 anos')