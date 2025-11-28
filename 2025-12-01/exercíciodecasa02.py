'''
   Faça um programa que solicite 5 nomes de alunos e suas respectivas notas da 
   etapa 1 e da etapa 2.

   Armazene essas informações em listas separadas.
      - Nomes dos alunos -> lstNomes
      - Notas da etapa 1 -> lstNotas1
      - Notas da etapa 2 -> lstNotas2
   
   Após a entrada dos dados, o programa deve calcular a média (IFRN) de cada aluno e 
   armazená-la em uma nova lista.
      - Médias dos alunos -> lstMedias

   A média deve ser calculada pela fórmula:
      Média = (Nota Etapa 1 * 2) + (Nota Etapa 2 * 3) / 5

   No final, imprima o nome de cada aluno junto com suas notas e suas médias.

   Exemplo:
      Nome do Aluno          Etapa 1    Etapa 2    Média
      --------------------------------------------------
      João Silva             75         80         78
      Maria Oliveira         90         85         88
      Pedro Santos           60         70         65
      Ana Costa              85         90         88
      Lucas Pereira          70         75         73
      --------------------------------------------------
'''
lstNomes = list()
lstNotas1 = list()
lstNotas2 = list()
lstMedias = list()
for i in range(1):
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a nota da etapa 1: '))
    nota2 = float(input('Digite a nota da etapa 2: '))
    lstNomes.append(nome)
    lstNotas1.append(nota1)
    lstNotas2.append(nota2)
    media = ((nota1 * 2) + (nota2 * 3)) / 5
    lstMedias.append(media)
print('-='*30)
print('Nome do Aluno       Etapa 1     Etapa 2        Média')
print('-'*60)
for a in range(1):
    print(f'{lstNomes[a]}          {lstNotas1[a]:<10}     {lstNotas2[a]:<10}     {lstMedias[a]}')
print('-='*30)