# numeros = list()
# limite = 100

# for valor in range(limite):
#     numeros.append(valor)
# print(numeros)

# valor = 0
# while valor<limite:
#     numeros.append(valor)
#     valor+=1

# for v in numeros:
#     print(v)
#     if v%2 == 0:
#         print(f'{v} é par')
#     else:
#         print(f'{v} é ímpar')

# pas = 0
# while pas < len(numeros):
#     if numeros[pas]%2 == 0:
#         print(f'{numeros[pas]} é par')
#     else:
#         print(f'{numeros[pas]} é ímpar')
#     pas+=1

# import sys
# try:
#     limite = int(input('Digite o limite: '))
#     if limite < 0:
#         sys.exit('O limite deve ser um número positivo!')
# except ValueError:
#     sys.exit('O limite deve ser um número inteiro!')
# except Exception as ERRO:
#     sys.exit(f'ERRO: {ERRO}')
# else:
#     multiplos = list()
#     for i in range(0, limite):
#         if i%6 == 0:
#             multiplos.append(i)
#     print(multiplos)