'''
   Desenvolva um código em Python que solicite ao usuário que informe os 
   comprimentos dos três lados de um triângulo. 
   
   Em seguida, verifique se esses comprimentos podem formar um triângulo. 
   Caso afirmativo, calcule e informe os valores dos ângulos do triângulo e 
   classifique-o quanto aos lados e aos ângulos.

   Instruções:
      - Peça ao usuário para inserir os comprimentos dos três lados do triângulo;
      - Verifique se os comprimentos fornecidos podem formar um triângulo. 
        Caso contrário, informe que não é possível formar um triângulo com esses lados;
      - Se for possível formar um triângulo, calcule os três ângulos do triângulo;
      - Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) 
        e aos ângulos (agudo, obtuso ou retângulo);
      - Exiba a classificação do triângulo quanto aos lados e aos ângulos.

   Observações:
      - Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, 
        é necessário verificar a seguinte condição: A soma de quaisquer dois lados de 
        um triângulo deve ser sempre maior que o terceiro lado;
      - Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo;
      - Para classificar quanto aos lados, verifique se os três lados são iguais 
        (equilátero), se dois lados são iguais (isósceles) ou se todos os lados são 
        diferentes (escaleno);
      - Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 
        90 graus (obtuso), se um dos ângulos é igual a 90 graus (retângulo) 
        ou se todos os ângulos são menores que 90 graus (agudo);
      - Considere que os ângulos são expressos em graus.

   Dica: Utilize a biblioteca math.
   https://docs.python.org/3/library/math.html
'''

import sys
import math

try:
    ladoA = float(input('Digite o valor lado A do triângulo: '))
    ladoB = float(input('Digite o valor lado B do triângulo: '))
    ladoC = float(input('Digite o valor lado C do triângulo: '))

except ValueError:
    sys.exit('ERRO: Digite um valor válido!')

except Exception as strErro:
    sys.exit(f'ERRO: {strErro}!')

else:
    if ladoA < ladoB+ladoC and ladoB < ladoA+ladoC and ladoC < ladoA+ladoB:
      print('É possível formar um triângulo') 
      cossA = math.cos(math.radians(ladoA))
      cossB = math.cos(math.radians(ladoB)) 
      cossC = math.cos(math.radians(ladoC))
      print(f'O ângulo do lado A {ladoA} é {cossA:.1f}')
      print(f'O ângulo do lado B {ladoB} é {cossB:.1f}')
      print(f'O ângulo do lado C {ladoC} é {cossC:.1f}')

      print('Quanto aos lados:')

      if ladoA == ladoB == ladoC:
          print('O triângulo é equilátero')
      elif ladoA != ladoB != ladoC != ladoA:
          print('O triângulo é escaleno')
      else:
          print('O triângulo é isósceles')

      print('Quanto aos ângulos:')

      if cossA > 90 or cossB > 90 or cossC > 90:
          print(f'O ângulo é obtuso') 
      elif cossA == 90 or cossB == 90 or cossC == 90:
          print('O ângulo é retângulo')
      else:
          print('O ângulo é agudo')

    else:
        print('Não é possível formar um triângulo')
    

