'''
   Fazer um programa que solicite ao usuário um valor inteiro positivo N e gere uma lista 
   com N valores inteiros aleatórios entre 1 e 100, sem repetição. 
   
   Em seguida, o programa deve exibir:

   - A lista gerada
   - A soma dos valores na lista
   - A média dos valores na lista
   - O maior valor na lista
   - O menor valor na lista
   - A mediana dos valores na lista
   - A variância dos valores na lista
   - O desvio padrão dos valores na lista
'''
from base64 import standard_b64decode
import random
from statistics import median, variance
valores = 20
lista_valores = list()
while valores > 0:
    val = random.randint(1, 100)
    if val not in lista_valores:
        lista_valores.append(val)
        valores -= 1
print(f'O tamanho da lista é {len(lista_valores)}')
print(f"A lista gerada é {lista_valores}")
print(f'A soma da lista é {sum(lista_valores)}')
print(f'A média da lista é {sum(lista_valores)/len(lista_valores)}')
print(f'O maior valor da lista é {max(lista_valores)}')
print(f'O menor valor da lista é {min(lista_valores)}')
print(f'A mediana dos valores da lista é {median(lista_valores)}')
print(f'A variância dos valores da lista é {variance(lista_valores):.1f}')
print(f'O desvio padrão dos valores da lista é {variance(lista_valores)**2:.2f}')

# import sys, random
# try:
#      valores = 20
# except ValueError:
#     sys.exit('ERRO: O valor deve ser inteiro!')
# except Exception as ERRO:
#     sys.exit(f'ERRO: {ERRO}')
# else:
#     continue