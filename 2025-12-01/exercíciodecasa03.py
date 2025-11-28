'''
   Reescreva o código do exercício anterior, mas desta vez utilizando listas
   compostas (listas dentro de listas) para armazenar as informações dos alunos.
'''
lstAlunos = list()
for i in range(5):
    nome = str(input('Digite o nome do aluno: '))
    nota1 = int(input('Digite a nota da etapa 1: '))
    nota2 = int(input('Digite a nota da etapa 2: '))
    media = ((nota1 * 2) + (nota2 * 3)) / 5
    lstAlunos.append([nome, nota1, nota2, media])
print('-='*30)
print('Nome do Aluno       Etapa 1     Etapa 2        Média')
print('-'*60)
for lstAlunos in lstAlunos:
    nome = lstAlunos[0]
    nota1 = lstAlunos[1]
    nota2 = lstAlunos[2]
    media = lstAlunos[3]
    print(f'{nome}     {nota1}       {nota2}       {media}')
print('-='*30)