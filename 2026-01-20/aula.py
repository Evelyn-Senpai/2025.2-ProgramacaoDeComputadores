'''
Um dicionário (dict) é uma coleção não ordenada (antes do Python 3.7) ou ordenada por inserção (Python 3.7+) de pares chave-valor. 

Diferentemente das listas, onde acessamos os elementos por um índice numérico sequencial (0, 1, 2...), nos dicionários o acesso é feito através de uma chave exclusiva definida pelo programador.
'''

def cores(cor = 'sem'):
    cores = {
        'sem': '\033[m',
        'vermelho': '\033[31m',
        'verde': '\033[32m'
    }
    return cores[cor]

import sys

dictAlunos = dict()
listAlunos = list()

try:
    for i in range(1):
        dictAlunos['matricula'] = int(input('Matricula: '))
        dictAlunos['nome'] = str(input('Nome: ')).strip()
        dictAlunos['campus'] = str(input('Campus: ')).strip()
        dictAlunos['curso'] = str(input('Curso: ')).strip()
        listAlunos.append(dictAlunos.copy())

except Exception as Erro:
    sys.exit(f'{cores("vermelho")}Erro: {Erro}{cores("sem")}')

else:
    print(f'{cores("verde")}{listAlunos}{cores("sem")}')
