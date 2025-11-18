frase = 'Curso Python'

# FATIAMENTO 
# Pegando a posição que está o caracter
print(frase[2]) 
# Pegando intervalos de caracters
print(frase[2:12])
# Pegando intervalos de caracters de 2 em 2
print(frase[2:12:2])
# Pegando intervalos de caracters do 0 até o caracter escolhido
print(frase[:5])
# Pegando intervalos de caracters do caracter escolhido até o final
print(frase[6:])
# Pegando intervalos de caracters do caracter escolhido até o final pulando de 3 em 3
print(frase[0::3])

# ANÁLISE
# Mostra a quantidade de caraters
print(len(frase))
# Mostrar a quantidade do caracter escolhido
print(frase.count('o'))
# Mostrar a quantidade do caracter escolhido com intervalos
print(frase.count('o',0,9))
# Mostrar a quantidade de caractes achados
print(frase.find('urso'))
# Mostrar se existe a frase escolhida
print('Curso' in frase)

# TRANSFORMAÇÃO
# Substituição de caracters
print(frase.replace('Python', 'Android'))
# Transforma os caracters em maiusculos
print(frase.upper())
# Transforma os caracters em minusculas
print(frase.lower())
# Transforma os caracters em minusculas exeto o primeiro
print(frase.capitalize())
# Transforma o primeiro caracter de todas as palavras em maiusculas
print(frase.title())
frase2 = '   Python é legal   '
# Remove os espaços inúteis no inicio e no final da frases
print(frase2.strip())
# Remove somente os espaços inúteis do final da frases
print(frase2.rstrip())
# Remove somente os espaços inúteis do inicio da frases
print(frase2.lstrip())

# DIVISÃO
# Cria uma divisão entre os espaços na frase
print(frase.split())

# JUNÇÃO
# Separada os elementos com o caracter desejado
print('-'.join(frase))