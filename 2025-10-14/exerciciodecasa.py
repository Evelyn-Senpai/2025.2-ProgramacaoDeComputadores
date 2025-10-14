'''
   Escreva um programa que pede ao usuário para inserir um ano e 
   determina se ele é bissexto ou não. 
   
   Um ano é bissexto se atender a uma das seguintes regras:

      - É divisível por 4, mas não é divisível por 100.

      - É divisível por 400.

      (Por exemplo, 2000 e 2400 são bissextos; 1800, 1900 e 2100 não são). 
      
   O programa deve exibir "O ano [ano] é bissexto." ou 
   "O ano [ano] não é bissexto.". 
   
   Use try...except para validar a entrada.
'''

import sys

try:

   ano = int(input('Digite um ano: '))

   if ano < 0:
      raise FloatingPointError
except FloatingPointError:
   sys.exit('ERRO: Digite um valor maior que 0!')

except ValueError:
   sys.exit('ERRO: Digite um valor válido!')

except Exception as strErro:
   sys.exit(f'ERRO: {strErro}')

else:
   print(f'o ano {ano} é bissexto')
   print(f'O ano {ano} não é bissexto')