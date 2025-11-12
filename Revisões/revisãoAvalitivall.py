# import sys
# soma = 0
# quantidade = 0
# maior = 0
# menor = 0
# while True:
#     try:
#         numero = int(input('Digite um número: '))
#         if numero < 0:
#             sys.exit('ERRO: Deve ser um número positívo!')
#         if numero == 0:
#             break
#     except ValueError:
#         print('ERRO: Deve ser um número inteiro!')
#     except Exception as ERRO:
#         sys.exit(f'ERRO: {ERRO}')
#     else:
#         soma += numero
#         quantidade += 1
#         media = soma/quantidade
#         if quantidade == 1:
#             maior = menor = numero
#         else:
#             if numero > maior:
#                 maior = numero
#             elif numero < menor:
#                 menor = numero
# print(f'A soma dos número é {soma}\nForam digitados {quantidade} números\nA média dos número é {media:.2f}\nO maior é {maior}\nO menor é {menor}')



# str = 'X-DSPAM-Confidence:0.8475'
# posicao = str.find(':')
# numero = str[posicao + 1:]
# print(float(numero))