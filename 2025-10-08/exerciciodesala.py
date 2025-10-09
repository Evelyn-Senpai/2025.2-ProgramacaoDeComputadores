'''

   Faça um programa que solicite ao usuário um número de até 4 dígitos inteiro positivo e exiba a soma dos seus algarismos.

   Exemplo: 2456 = 17 (2 + 4 + 5 + 6)

   DICA: Vocês irão usar o operador de divisão inteira (//) e o operador de resto de divisão inteiro (%)

'''

import sys 

try: 
    numero = int(input('Digite um número de até 4 digitos inteiro positivo: ')) 
    
    if numero < 0: 
        raise FloatingPointError 

except FloatingPointError: 
    sys.exit('Digite um número positivo!') 

except ValueError: 
    sys.exit('Digite um número inteiro!') 
    
else: 
    u = numero // 1 % 10 
    d = numero // 10 % 10 
    c = numero // 100 % 10 
    m = numero // 1000 % 10 
    
    soma = u+d+c+m 
    
    print(f'{numero} = {soma} ({m}+{c}+{d}+{u})')