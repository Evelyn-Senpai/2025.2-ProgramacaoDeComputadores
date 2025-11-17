'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000.
c) Qual é o nome do produto mais barato.
'''
total_da_compra = maior_1000  = preco_barato = cont = 0
produto_barato = ' '
print('-'*40)
print('LOJA SUPER BARATÃO')
print('-'*40)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total_da_compra += preco
    if preco > 1000:
        maior_1000 += 1
    if cont == 1 or preco < preco_barato:
        preco_barato = preco
        produto_barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-'*20, 'FIM DO PROGRAMA', '-'*20)
print(f'O total da compra foi R$ {total_da_compra:.2f}')
print(f'Temos {maior_1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R$ {preco_barato:.2f}')