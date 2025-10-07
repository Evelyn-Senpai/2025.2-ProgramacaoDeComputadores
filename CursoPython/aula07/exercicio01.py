# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa. O salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode excerder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))

prestacao =  casa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de {:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,anos,prestacao))

if prestacao <= minimo:
    print('EMPRÉSTIMO CONCEDIDO.')
else:
    print('EMPRÉSTIMO NEGADO.')


