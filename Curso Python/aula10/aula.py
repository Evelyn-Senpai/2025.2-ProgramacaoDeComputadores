n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('Soma = %s' % (s)) # PYTHON 2
# print('Soma = {}'.format(s)) # PYTHON 3
print(f'Soma = {s}') # PYTHON 3.6+