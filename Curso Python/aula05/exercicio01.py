#  Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras miúsculas: {}'.format(nome.lower()))
print('A quantidade de letras no seu nome é: {}'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('A quantidade de letras no seu primeiro nome é: {}'.format(len(separa[0])))