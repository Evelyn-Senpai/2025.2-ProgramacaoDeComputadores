'''
   Fazer um programa que leia o arquivo capitais_brasil.csv e
   preencha uma lista com sublistas contendo o nome da capital, 
   a sigla do seu estado, a sigla da sua região e a sua população.

   Após gerar a lista, gere uma lista contendo a sigla da região
   e o total da população das capitais daquela região.

   Em seguida salve o resultado em um arquivo chamado populacao_regioes.csv,
   no mesmo diretório onde se encontra o programa, no seguinte formato 
   (os valores abaixo são apenas ilustrativos):

   Região;População
   N;123456
   NE;234567
   CO;345678
   S;456789
   SE;567890
   
   Não use bibliotecas para manipulação de arquivos CSV.
'''
import sys, os
try:
    diretorio = open(os.path.dirname(__file__))
    leitura = open(f'{diretorio}\\capitais_brasil.csv', 'r')
except Exception as Erro:
    sys.exit(f'\033[31mERRO: {Erro}!\033[m')
else:
    lista_principal = list()
    lista_estado = list()
    lista_sigla = list()
    lista_regiao = list()
    lista_populacao = list()
    while True:
        linha = leitura.readline().strip()
        if not linha: break
        try:
            lista_estado.append(linha[0])
            lista_sigla.append(linha[1])
            lista_regiao.append(linha[2])
            lista_populacao.append(linha[3])

            lista_principal.append(lista_estado[:])
            lista_principal.append(lista_sigla[:])
            lista_principal.append(lista_regiao[:])
            lista_principal.append(lista_populacao[:])
        except Exception as Erro:
            sys.exit(f'ERRO: {Erro}!')
    leitura.close()
    print(lista_principal)
    print('\033[32mDeu certo\033[m')