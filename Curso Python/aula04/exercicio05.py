# Faça uma lista que leia os valores em ordem aleatória.
import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundp aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem será:')
print(lista)