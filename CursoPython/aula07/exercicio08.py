# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

valor = float(input('Valor das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] À vista dinheiro/cheque\n[ 2 ] À vista no cartão\n[ 3 ] 3x ou mais no cartão\n[ 4 ] 2x no cartão')
cond = int(input('Qual é a opção? '))

if cond == 1:
    preco = valor - (valor*10/100)
    print('O preço final é R${:.2f}'.format(preco))
elif cond == 2:
    preco = valor - (valor*5/100)
    print('O preço final é R${:.2f}'.format(preco))
elif cond == 3:
    parcelas = int(input('Quantas parcelas? '))
    preco = valor + (valor*20/100)
    q_parcelas = preco/parcelas
    print('Com {} parecelas de R${:.2f} com juros\nO preço final é R${:.2f}'.format(parcelas,q_parcelas,preco))
elif cond == 4:
    q_parcelas = valor/2
    print('Com 2x parcelas de R${:.2f}\nO preço final é R${:.2f}'.format(q_parcelas,valor))