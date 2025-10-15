# Refaça o exercício05 da aula03, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número: '))
print('Sua tabuada é: ')
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
