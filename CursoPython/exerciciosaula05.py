#  Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.
# nome = str(input('Digite seu nome completo: ')).strip()
# print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
# print('Seu nome com todas as letras miúsculas: {}'.format(nome.lower()))
# print('A quantidade de letras no seu nome é: {}'.format(len(nome) - nome.count(' ')))
# separa = nome.split()
# print('A quantidade de letras no seu primeiro nome é: {}'.format(len(separa[0])))

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# n1 = int(input('Digite um número entre 0 e 9999: '))
# u = n1 // 1 % 10
# d = n1 // 10 % 10
# c = n1 // 100 % 10
# m = n1 // 1000 % 10
# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhares: {}'.format(m))


# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
# cidade = str(input('Digite o nome de uma cidade: ')).strip()
# print('Essa cidade começa com o nome Santo? {}'.format(cidade[:5].upper() == 'SANTO'))


# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
# frase = str(input('Digite uma frase: ')).upper()
# print('A quantidade de vezes que aparece a letra "a" é: {}'.format(frase.count('A')))
# print('O primeiro "a" aparece na posição {}'.format(frase.find('A')+1))
# print('O último "a" aparece na posição {}'.format(frase.rfind('A')+1))


# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n)-1]))
