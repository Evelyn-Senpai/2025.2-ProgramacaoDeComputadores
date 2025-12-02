'''
   Escreva um programa que construa uma lista de sub-listas de números inteiros.

   - O usuário deverá informar quantas sub-listas deseja gerar;
   - A primeira sub-lista deve ser [1, 1];
   - Cada nova sub-lista deve ser formada acrescentando ao final da lista anterior 
     a soma dos dois últimos números já existentes;
   - O processo deve continuar até que seja atingida a quantidade de sub-listas 
     definida pelo usuário.
   - Ao final, o programa deve imprimir todas as sub-listas geradas.

   Exemplo de saída para 5 sub-listas:

      [1, 1]
      [1, 1, 2]
      [1, 1, 2, 3]
      [1, 1, 2, 3, 5]
      [1, 1, 2, 3, 5, 8]
'''
import sys
try:
    numero = int(input('Quantas sub-listas você deseja gerar? '))
    if numero < 0:
        sys.exit('ERRO: O número deve ser positivo!')
except ValueError:
    sys.exit('ERRO: O número deve ser inteiro!')
except Exception as ERRO:
    sys.exit(f'ERRO: {ERRO}')
else:
    lista = []
    sub_lista = [1, 1]
    for l in range(numero):
        lista.append(sub_lista[:])
        soma = sub_lista[-1] + sub_lista[-2]
        sub_lista.append(soma)
    for sub in lista:
        print(sub)