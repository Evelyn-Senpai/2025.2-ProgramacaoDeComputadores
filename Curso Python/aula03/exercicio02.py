# Crie um algoritmo que leia um número e mostre o seu dobro, tríplo e raiz quadrada.
n1 = int(input('Digite um valor: '))
dob = n1*2
trip = n1*3
raq = n1**(1/2)
print('O dobro deste número é: {}\nO tríplo deste valor é: {}\nA raiz quadrada deste valor é: {:.2f}'.format(dob,trip,raq))