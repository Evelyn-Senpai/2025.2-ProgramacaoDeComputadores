'''
   Faça um programa que solicite ao usuário um número inteiro e 
   informe em quantas interações ele converge para a constante de 
   Kaprekar (6174). Lembre-se que o número não deve ter 4 dígitos 
   iguais. Caso o número não atenda a essa condição, informe
   que ele é inválido.

   O que é a constante de Kaprekar?
   A constante de Kaprekar é o número 6174, que é alcançado através
   de um processo repetitivo de manipulação de números de 4 dígitos.

   Como funciona o processo de Kaprekar:
   1. Pegue qualquer número de 4 dígitos com pelo menos dois dígitos diferentes.
   2. Ordene os dígitos em ordem crescente e decrescente para formar dois números diferentes.
   3. Subtraia o menor número do maior número.
   4. Repita o processo com o resultado até chegar a 6174.

   Exemplo:
   - Comece com o número 3524.
   - Ordene os dígitos: 5432 (decrescente) e 2345 (crescente).
     1ª iteração: 5432 - 2345 = 3087
   - Repita o processo:
     2ª iteração: 8730 - 0378 = 8352
     3ª iteração: 8532 - 2358 = 6174
'''
import sys
try: 
    numero = int(input('Informe um valor inteiro: '))
    if numero < 0:
        sys.exit('ERRO: O valor informado deve ser maior que 0!')
except ValueError:
    sys.exit('ERRO: O valor informado deve ser inteiro!')
except Exception as Erro:
    sys.exit(f'ERRO: {Erro}')
else:
    if numero < 1000 or numero > 9999:
        sys.exit(f'O valor informado deve ter exatamente quatro digitos!')
    numero_str = str(numero)
    if numero_str.count(numero_str[0]) == 4:
        sys.exit(f'O valor informado não pode ter os quatro digitos iguais!')
    print('Deu certo')
    # numero_ordenado_str = sorted(numero_str)
    # numero_ordenado_inverso_str = sorted(numero_ordenado_str)

    # inverso_str = numero_str[::-1]
    # inverso = int(inverso_str)
    # subtracao = numero - inverso
    # # print(f'{numero} - {inverso} = {subtracao}')