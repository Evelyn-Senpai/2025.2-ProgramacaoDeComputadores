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
    if n < 0:
        sys.exit('ERRO: O valor deve ser maior ou igual a zero!')
except ValueError:
    sys.exit('ERRO: Informe um valor inteiro!')
except:
    sys.exit(f'ERRO: {sys.exc_info()}')
else:
    for f in range(1, n+1):
        print(f'{f}')
        f1 = f*(n-1)
        f2 = f*(n-2)
        f = f1 + f2
print('FIM')