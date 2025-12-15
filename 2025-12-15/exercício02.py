'''
   Fazer um programa que leia o arquivo valores_2.txt, que contém números inteiros,
   um por linha, e calcule a soma desses números. O programa deve exibir o resultado na tela.
'''
import os, sys

try:
    diretorio = os.path.dirname(__file__)
    arqLeitura = open(f'{diretorio}\\valores_2.txt', 'r')
except FileNotFoundError:
    sys.exit('\033[31mArquivo não encontrado.\033[m')
except Exception as Erro:
    sys.exit('Erro: {Erro}.')
else:
    lista = list()
    while True:
        linha = arqLeitura.readline().strip()
        valor = int(linha)
        lista.append(valor)
        if not linha.isalpha() : break
    arqLeitura.close()
    print(f'\033[32m{lista}.\033[m')