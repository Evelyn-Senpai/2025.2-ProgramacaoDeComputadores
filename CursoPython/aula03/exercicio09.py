# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Digite seu salário: R$'))
aum = (15*sal)/100
salaum = aum+sal
print('Com 15% de aumento fica: RS{:.2f}'.format(salaum))