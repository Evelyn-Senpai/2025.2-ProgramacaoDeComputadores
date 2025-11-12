'''
01
'''
# import sys
# soma = 0
# quantidade = 0
# maior = 0
# menor = 0
# while True:
#     try:
#         numero = int(input('Digite um número: '))
#         if numero < 0:
#             sys.exit('ERRO: Deve ser um número positívo!')
#         if numero == 0:
#             break
#     except ValueError:
#         print('ERRO: Deve ser um número inteiro!')
#     except Exception as ERRO:
#         sys.exit(f'ERRO: {ERRO}')
#     else:
#         soma += numero
#         quantidade += 1
#         media = soma/quantidade
#         if quantidade == 1:
#             maior = menor = numero
#         else:
#             if numero > maior:
#                 maior = numero
#             elif numero < menor:
#                 menor = numero
# print(f'A soma dos número é {soma}\nForam digitados {quantidade} números\nA média dos número é {media:.2f}\nO maior é {maior}\nO menor é {menor}')
'''
02
'''
# str = 'X-DSPAM-Confidence:0.8475'
# posicao = str.find(':')
# numero = str[posicao + 1:]
# print(float(numero))
'''
03
'''
# import sys
# try:
#     numero = int(input('Digite um número: '))
#     if numero < 0:
#         sys.exit('ERRO: O número deve ser positívo!')
# except ValueError:
#     sys.exit('ERRO: O número deve ser inteiro!')
# except Exception as ERRO:
#     sys.exit(f'ERRO: {ERRO}')
# else:
#     for contador in range(1, 11):
#         multiplicacao = numero * contador
#         print(f'{numero} x {contador} = {multiplicacao}')
    
#     contador = 1
#     while contador <= 10:
#         multiplicacao = numero * contador
#         print(f'{numero} x {contador} = {multiplicacao}')
#         contador += 1
'''
04
'''
# import sys
# try:
#     soma_par = 0
#     soma_impar = 0

#     print('Os números pares são: ')
#     for contador in range(1, 51):
#         if contador % 2 == 0:
#             print(contador, end=' ')
#             soma_par += contador

#     contador = 1
#     while contador <= 50:
#         if contador % 2 == 0:
#             print(contador, end=' ')
#             soma_par += contador
#         contador += 1

#     print('\nOs números ímpares são: ')
#     for contador in range(1, 51):
#         if contador % 2 == 1:
#             print(contador, end=' ')
#             soma_impar += contador

#     contador = 1
#     while contador <= 50:
#         if contador % 2 == 1:
#             print(contador, end=' ')
#             soma_impar += contador
#         contador += 1
# except Exception as ERRO:
#     sys.exit(f'ERRO {ERRO}')
# else:
#     print(f'\nA soma dos pares é {soma_par}\nA soma dos ímpares é {soma_impar}')
'''
05
'''
# import sys
# try:
#     numero = int(input('Digite um número: '))
#     if numero < 0:
#         sys.exit('ERRO: Digite um número positivo!')
# except ValueError:
#     sys.exit('ERRO: DIgite um número inteiro!')
# except Exception as ERRO:
#     sys.exit(f'ERRO: {ERRO}')
# else:
#     if numero == 0 or numero == 1:
#         sys.exit(f'{numero}! = 1')
#     multiplicacao = 1

#     for contador in range(1, numero+1):
#         multiplicacao *= contador

#     contador = numero
#     while contador >= 1:
#         multiplicacao *= contador
#         contador -= 1
#     print(f'{numero}! = {multiplicacao}')
'''
06
'''
# import sys
# try:
#     numero = int(input('Digite um número: '))
#     if numero < 0:
#         sys.exit('ERRO: Digite um número positivo!')
# except ValueError:
#     sys.exit('ERRO: Digite um número inteiro!')
# except Exception as ERRO:
#     sys.exit(f'ERRO: {ERRO}')
# else:
#     f1 = 0
#     f2 = 1
#     print(f'{f1}, {f2}', end='')
#     # for contador in range(2, numero + 1):
#     #     soma = f1 + f2
#     #     print(f', {soma}', end='')
#     #     f1 = f2
#     #     f2 = soma

#     contador = 1
#     while contador <= numero:
#         soma = f1 + f2
#         print(f', {soma}', end='')
#         f1 = f2
#         f2 = soma
#         contador += 1
'''
07
'''
# import sys
# try:
#     numero = int(input('Digite um número: '))
#     if numero < 0:
#         sys.exit('ERRO: O número deve ser positivo!')
# except ValueError:
#     sys.exit('ERRO: Deve ser um número inteiro!')
# except Exception as ERRO:
#     sys.exit(f'ERRO {ERRO}')
# else:
#     if numero < 2:
#         sys.exit(f'{numero} não é primo')
#     quantidade = 0
#     for contador in range(1, numero+1):
#         if numero % contador == 0:
#             quantidade += 1
#         if quantidade > 2: break
    
#     if quantidade == 2:
#         print(f'{numero} é primo')
#     else:
#         print(f'{numero} não é primo')
'''
08
'''
import sys
try:
    numero = int(input('Digite um número: '))
    if numero < 0:
        sys.exit('ERRO: O número deve ser positivo!')
except ValueError:
    sys.exit('ERRO: Deve ser um número inteiro!')
except Exception as ERRO:
    sys.exit(f'ERRO: {ERRO}')
else:
    if numero < 1:
        sys.exit(f'{numero} não é triangular')
    triangular = 0
    incremento = 1
    while triangular < numero:
        triangular += incremento
        incremento += 1
    if triangular == numero:
        print(f'{numero} é triangular')
    else:
        print(f'{numero} não é triangular')