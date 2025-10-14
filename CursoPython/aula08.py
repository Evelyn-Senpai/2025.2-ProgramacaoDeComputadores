
# CONTANDO DE 1 ATÉ 10(O ÚLTIMO NÚMERO É IGNORADO)
# for c in range(1, 10):
#     print(c)
# print('Fim')

# SE QUISESSE CONTAR DE 1 ATÉ 10, SERIA:
# for c in range(1, 11):
#     print(c)
# print('Fim')

# DE FORMA DECRESCENTE
# for c in range(10, 0, -1):
#     print(c)
# print('Fim')

# DE FORMA CRESCENTE
# for c in range(1, 11, +1):
#     print(c)
# print('Fim')

# PULANDO DE 2 EM 2
# for c in range(0, 11, 2):
#     print(c)
# print('Fim')

# CONTANDO UM NÚMERO
# n = int(input('Digite um número: '))
# for c in range(1, n+1):
#     print(c)
# print('Fim')

# inicio = int(input('Inicio: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))
# for c in range(inicio, fim+1, passo):
#     print(c)
# print('Fim')

# INPUT DENTRO DO FOR
# for c in range(0, 3):
#     n = int(input('Digite um número: '))
# print('Fim')

# SOMA DE NÚMEROS DENTRO DO FOR
soma = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    soma += n
print('A soma dos números é {}'.format(soma))