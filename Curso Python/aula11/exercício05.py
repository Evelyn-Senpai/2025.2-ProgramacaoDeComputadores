'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
lista = ('Lápis', 1.75, 'Mochila', 120.32, 'Livro', 34.9, 'Borracha', 2, 'Estojo', 25,
         'compasso', 9.99, 'Canetas', 22.3, 'Transferidor', 4.20, 'Caderno', 15.9)
for produto in range(0, len(lista)):
    if produto % 2 == 0:
        print(f'{lista[produto]:.<30}', end='')
    else:
        print(f'R$ {lista[produto]:>7.2f}')
print('-'*40)