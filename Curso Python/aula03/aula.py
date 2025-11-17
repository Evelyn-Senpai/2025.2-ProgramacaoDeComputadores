# Adição +
# Subtração -
# Multiplicação *
# Divição /
# Potênciação ** ou pow(x,y)
# Divisão inteira //
# Resto da divisão %
# Igualdade ==

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1/n2
pot = soma**2
int = n1//n2
red = n1%n2
print('A soma dos valores é: {},\nA subtração dos valores é: {},\nA multiplicação dos valores é: {},\nA divição dos valores é: {:.3f}.'.format(soma,sub,mult,div), end = ' ')
print('\nA potênciação é: {},\nA divição inteira é {},\nO resto da divisão é {}'.format(pot,int,red))