'''
	Crie um programa em Python que calcule as raízes de uma equação do 2º grau.
	
	O programa deve:
	
		- Ler os valores de a, b e c como entrada;
		
		- Verificar se o valor de a é zero. Caso seja, a equação não será do 
		  2º grau e o programa deve informar o usuário sobre isso e encerrar;
		  
		- Calcular o discriminante(delta) e, com base no valor de delta:
			
			- delta > 0 : a equação possui duas raízes reais distintas. 
			  O programa deve calcular e exibir ambas as raízes;
			  
			- delta = 0 : a equação possui uma única raiz real. 
			  O programa deve calcular e exibir a raiz única;
			  
			- delta < 0 : a equação não possui raízes reais. 
			  O programa deve informar ao usuário que não existem raízes reais.
			  
		- Tratar as exceções devidas.
'''

import sys
from math import dist

try:
    a = int(input('Digite o valor de A: '))

    if a <= 0:
        raise FloatingPointError

except FloatingPointError:
    sys.exit('A equação não é de segundo grau. Informe valores maiores que zero!')

except ValueError:
    sys.exit('Informe valores inteiros!')

else:
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))

    delta = (b*b) - 4 * a * c
    raiz_de_delta = delta**(1/2)

    if delta > 0:
        raiz1 = (-b + raiz_de_delta)/(2*a)
        raiz2 = (-b - raiz_de_delta)/(2*a)
        print(f'{delta} {raiz_de_delta}')
        print(f'Para a equação {a} {b} {c}, as raizes são {raiz1} e {raiz2}')
    elif delta == 0:
        raiz1 = -b + raiz_de_delta/2*a
        print(f'Para a equação {a} {b} {c}, a raize é {raiz1}')
    else:
        print('A equação não possui raízes reais')


