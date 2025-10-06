# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço do produto: R$'))
desc = (5*p)/100
print('O produto com 5% de desconto fica: R${:.2f}'.format(p-desc))