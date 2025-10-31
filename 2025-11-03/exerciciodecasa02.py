'''
   Programa que solicita um número inteiro ao usuário e exiba os n
   primeiros elementos da Série de Fibonacci (usando FOR).

   Exemplo: n = 10

   Saída: 
      1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''
import sys
try:
    n = int(input('Informe um valor inteiro: '))
    if n <= 0:
        sys.exit('ERRO: O valor deve ser maior que zero!')
except ValueError:
    sys.exit('ERRO: Informe um valor inteiro!')
except Exception as Erro:
    sys.exit(f'ERRO: {Erro}')
else:
    f1 = 0
    f2 = 1
    cont = 3
    print(f'{f2}', end='')
    for f in range(cont, n + 2):
        f = f1 + f2
        print(f', {f}', end='')
        f1 = f2
        f2 = f
        cont += 1