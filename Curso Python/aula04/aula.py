import math
n1 = int(input('Digite um número: '))
raiz = math.sqrt(n1)
print('A raiz de {} é {}'.format(n1, math.ceil(raiz)))

from math import sqrt, ceil
n1 = int(input('Digite um número: '))
raiz = sqrt(n1)
print('A raiz de {} é {}'.format(n1, ceil(raiz)))

import random
n1 = random.randint(1, 10)
print(n1)

import emoji
print(emoji.emojize('Python é :thumbs_up:', language = 'alias'))