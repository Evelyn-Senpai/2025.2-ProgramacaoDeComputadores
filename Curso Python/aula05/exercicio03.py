# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('Essa cidade começa com o nome Santo? {}'.format(cidade[:5].upper() == 'SANTO'))