it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Excercises: Level 1
# 1 Find the length of the set it_companies
print(len(it_companies)) # 7

# 2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Mercado Libre', 'Uala'])
print(it_companies)

# 4 Remove one of the companies from the set it_companies
it_companies.remove('Uala') # se puede usar discard() o pop()
print(it_companies)

# 5 What is the difference between remove and discard
# it_companies.remove('Uala') # da error al no encontrarlo
it_companies.discard('Uala') # no da error

# Excersises: Level 2
# 1 Join A and B
C = A.union(B)
print(C) # {19, 20, 22, 24, 25, 26, 27, 28}

# 2 Find A intersection B
print(A.intersection(B)) # {19, 20, 22, 24, 25, 26}

# 3 Is A subset of B
print('level 2 3',A.issubset(B)) # True

# 4 Are A and B disjoint sets
print(A.isdisjoint(B)) # False

# 5 Join A with B and B with A
print(A.union(B)) # {19, 20, 22, 24, 25, 26, 27, 28}
print(B.union(A)) # {19, 20, 22, 24, 25, 26, 27, 28}

# 6 What is the symmetric difference between A and B
print(A.symmetric_difference(B)) # {27, 28}

# 7 Delete the sets completely
del A, B # borra los dos

# Exercises: Level 3
# 1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(age)) # 8
age = set(age)
print(len(age)) # 5 porque no hay repetidos

# 2 Explain the difference between the following data types: string, list, tuple and set
# string: cadena de texto, se pueden aplicar métodos. 
# list: [] se pueden cambiar. Varios tipos de items. Tienen index.
# tuple: () no se pueden cambiar. Varios tipos de items. Tienen index.
# set: {} se pueden cambiar. Solo un tipo de item. Sin index.

# 3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence = sentence.split(' ')
sentence = set(sentence)
print(sentence)
print(len(sentence)) # 10
