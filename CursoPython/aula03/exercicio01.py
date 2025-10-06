# Faça um programa que leia um número inteiro e mostre na telao seu sucessor e seu antecessor.
n1 = int(input('Digite um valor: '))
suc = n1+1
ant = n1-1
print('O antecessor desse número é: {}\nO sucessor desse número é: {}'.format(ant,suc))