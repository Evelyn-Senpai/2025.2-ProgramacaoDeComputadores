'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você vai mostrar, para cada palavra, quais são as suas vogais.
'''
lista = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programar', 'Futuro')
for palavra in lista:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')