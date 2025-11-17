# Crie um programa que leia quanto dinheiro uma pesssoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere USS1.00 = R$3.27
d = float(input('Digite quanto dinheiro você tem: R$'))
con = d/3.27
print('Você pode comprar USS{:.2f}'.format(con)) 