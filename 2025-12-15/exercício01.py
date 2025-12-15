'''
   Fazer um programa que leia o conteúdo do arquivo resumo_lotr.txt e imprima na tela.
'''
import os, sys

try:
    diretorio = os.path.dirname(__file__)
    arqLeitura = open(f'{diretorio}\\resumo_lotr.txt', 'r')
except FileNotFoundError:
    sys.exit('\033[31mArquivo não encontrado.\033[m')
except Exception as Erro:
    sys.exit('Erro: {Erro}.')
else:
    conteudo = arqLeitura.read()
    print(conteudo)
    arqLeitura.close()
    print('\033[32mDeu certo.\033[m')