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

import os, sys, statistics

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
    erros = 0
    while True:
        linha = arqLeitura.readline().strip()
        if not linha: break
        if linha.isnumeric():
            valor = int(linha)
            numeros.append(valor)
        try:
            valor = int(linha)
        except ValueError:
            print(f'ERRO: Valor inválido {linha} ignorado!')
            erros += 1
        except Exception as ERRO:
            print(f'ERRO: {ERRO} ao processar o valor {linha} foi ignorado!')
        numeros.append(valor)            
    arqLeitura.close()
    soma = sum(numeros)
    media = soma/len(numeros)

    mediana = statistics.median(numeros)
    variancia = statistics.variance(numeros)
    desvio = statistics.stdev(numeros)
    print(f'\033[32mA soma dos números é {soma}\033[m')
    print(f'\033[32mA média dos números é {media:.2f}\033[m')
    print(f'\033[32mA mediana dos números é {mediana:.2f}\033[m')
    print(f'\033[32mA variância dos números é {variancia:.2f}\033[m')
    print(f'\033[32mO desvio padrão dos números é {media:.2f}\033[m')
    print(f'\033[32mAs linhas ignoradas foram {erros}\033[m')
    try:
        
        saida = open(f'{diretorio}\\resultados_2.txt', 'w', encoding='utf-8')
    except FileNotFoundError:
        sys.exit('\033[31mArquivo não encontrado.\033[m')
    except Exception as Erro:
        sys.exit('\033[31mErro: {Erro}.\033[m')
    else:
        saida.write(f'\033[32mA soma dos números é {soma}\033[m\n')
        saida.write(f'\033[32mA média dos números é {media:.2f}\033[m\n')
        saida.write(f'\033[32mA mediana dos números é {mediana:.2f}\033[m\n')
        saida.write(f'\033[32mA variância dos números é {variancia:.2f}\033[m\n')
        saida.write(f'\033[32mO desvio padrão dos números é {media:.2f}\033[m\n')
        saida.write(f'\033[32mAs linhas ignoradas foram {erros}\033[m')
        saida.close()    