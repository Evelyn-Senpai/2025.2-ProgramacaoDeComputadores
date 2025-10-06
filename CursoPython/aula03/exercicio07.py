# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinte para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l*a
tint = area/2
print('A área da sua parede é: {:.1f} m² e é necessario {:.1f} litros de tinta para pintá-la.'.format(area,tint))