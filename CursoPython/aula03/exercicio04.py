# Escreve um programa que leia um valor em metros e o exiba convertido em centrímetros e milímetros.
v1 = int(input('Digite um valor em metros: '))
cm = v1*100
mm = v1*1000
print('Metros = {:.0f}\nCentrímetros = {:.0f}\nMilímetros = {}'.format(v1,cm,mm))