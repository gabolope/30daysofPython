print('\n### Level 1 ###')
# Exercises: Level 1
# 1 What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

import re
from collections import Counter

separator = r'[^\W]+' #\W significa cualquier caracter que no sea letra, numero o _. Y el + indica que se haga una o mas veces. El [^] indica el negativo de esto. 
separator2 = r'[a-zA-z]+'

paragraph_lt = re.findall(separator, paragraph) # guardo las palabras en una lista
word_count_dt = Counter(paragraph_lt) # realizo un conteo de cada palabra. Esto devuelve un dict
word_count_lt = list(word_count_dt.items()) # paso el dict a list
word_count_sorted = sorted(word_count_lt, key = lambda x: x[1], reverse= True) # ordeno la lista de mayor a menor segun el numero de repeticiones

print('#1:', word_count_sorted)

# 2 The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'

separator = r'-\d+|\d+' # tomo los numeros negativos y los numeros positivos
numbers = re.findall(separator, text) # busco en el texto
numbers_int = [int(num) for num in numbers] # paso los string de los numeros a int

min = min(numbers_int)
max = max(numbers_int)
distance = abs(min) + max

print(f'The distance between the two furthest particles is: {distance}')


print('\n### Level 2 ###')
# Exercises: Level 2
# 1 Write a pattern which identifies if a string is a valid python variable

str1 = '10_primeros_paises'
str2 = 'paises+ciudades'
str3 = 'mejores paises'
str4 = 'mejores_paises'
str5 = 'def'
str6 = 'class'

# dar condiciones para que devuelva nombres validos dentro de un texto.
valid = r'^\d'

print('\n### Level 3 ###')
# Exercises: Level 3
# 1 Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

