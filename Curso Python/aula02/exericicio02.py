#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçãoes possiveis sobre ele.
n = input('Digite qualquer coisa: ')
print('O tipo primitivo dessa valor é: ', type(n))
print('É alfabetico? ', n.isalpha())
print('É um número? ', n.isnumeric())
print('É alfanumérico? ', n.isalnum())
print('É maiúsculo? ', n.isupper())
print('É minúsculo? ', n.islower())
print('É capitalizada? ', n.istitle())