'''
   Fazer um programa que leia o arquivo valores_1.txt, que contém números 
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

import os, sys, statistics

try:
    diretorio = os.path.dirname(__file__)
    arqLeitura = open(f'{diretorio}\\valores_1.txt', 'r')
except FileNotFoundError:
    sys.exit('\033[31mERRO: Arquivo não encontrado!\033[m')
except Exception as Erro:
    sys.exit('\033[31mERRO: {Erro}.\033[m')
else:
    numeros = list()
    erros = 0
    while True:
        linha = arqLeitura.readline().strip()
        if not linha: break
        try:
            valor = int(linha)
            numeros.append(valor)
        except ValueError:
            print(f'\033[31mERRO: Valor inválido {linha} ignorado!\033[m')
            erros += 1
        except Exception as ERRO:
            print(f'\033[31mERRO: {ERRO} ao processar o valor {linha} foi ignorado!\033[m')
    arqLeitura.close()
    soma = sum(numeros)
    media = soma/len(numeros)

    maiores = 0
    menores = 0
    for i in numeros:
        if i > media:
            maiores += 1
        elif i < media:
            menores += 1

    mediana = statistics.median(numeros)
    variancia = statistics.variance(numeros)
    desvio = statistics.stdev(numeros)
    try:    
        saida = open(f'{diretorio}\\resultados.txt', 'w', encoding='utf-8')
    except FileNotFoundError:
        sys.exit('\033[31mArquivo não encontrado!\033[m')
    except Exception as Erro:
        sys.exit(f'\033[31mErro: {Erro}!\033[m')
    else:
        saida.write(f'A soma dos números é {soma}.\n')
        saida.write(f'A média dos números é {media:.2f}.\n')
        saida.write(f'A mediana dos números é {mediana:.2f}.\n')
        saida.write(f'Há {maiores} números maiores que a média.\n')
        saida.write(f'Há {menores} números menores que a média.\n')
        saida.write(f'A variância dos números é {variancia:.2f}.\n')
        saida.write(f'O desvio padrão dos números é {desvio:.2f}.\n')
        saida.write(f'As linhas ignoradas foram {erros}.\n')
        saida.close()
    
    print('\033[32mValores foram adicionados.\033[m')
