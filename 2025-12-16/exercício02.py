'''
   Fazer um programa que leia o arquivo valores_2.txt, que contém números 
   inteiros, um por linha, gere uma lista contendo os números lidos.
   
   Após a leitura, calcule:

   a) A soma dos números;
   b) A média dos números;
   c) Quantos números são maiores que média;
   d) Quantos números são menores que média;
   e) A mediana dos números;
   f) A variância dos números;
   g) O desvio padrão dos números.

   Escreva os resultados em um arquivo chamado resultados.txt.
'''

import os, sys

try:
    diretorio = os.path.dirname(__file__)
    arqLeitura = open(f'{diretorio}\\valores_2.txt', 'r')
except FileNotFoundError:
    sys.exit('\033[31mArquivo não encontrado.\033[m')
except ValueError:
    sys.exit('\033[31mValor não suportado.\033[m')
except Exception as Erro:
    sys.exit('Erro: {Erro}.')
else:
    numeros = list()
    while True:
        linha = arqLeitura.readline().strip()
        if not linha: break
        if linha.isnumeric():
            valor = int(linha)
            numeros.append(valor)
    arqLeitura.close()
    print('\033[32mDeu certo\033[m')
