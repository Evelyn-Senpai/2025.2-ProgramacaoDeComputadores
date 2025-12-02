'''
   Escreva um programa que construa uma lista de sub-listas de números inteiros.

   - O usuário deverá informar quantas sub-listas deseja gerar;
   - A primeira sub-lista será obrigatoriamente [1, 1];
   - Cada nova sub-lista deve começar e terminar com o número 1;
   - Os valores internos de cada sub-lista devem ser obtidos somando pares de números 
     vizinhos da sub-lista imediatamente anterior;
   - O processo deve continuar até que seja atingida a quantidade de sub-listas 
     definida pelo usuário;
   - Ao final, o programa deve imprimir todas as sub-listas geradas.

   Exemplo de saída para 5 sub-listas:

      [1, 1]
      [1, 2, 1]
      [1, 3, 3, 1]
      [1, 4, 6, 4, 1]
      [1, 5, 10, 10, 5, 1]
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
        lista_auxiliar = [1]
        for i in range(len(sub_lista)-1):
            lista_auxiliar.append(sub_lista[i] + sub_lista[i+1])
        lista_auxiliar.append(1)
        sub_lista = lista_auxiliar
    for sub in lista:
        print(sub)