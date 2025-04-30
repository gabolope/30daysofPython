countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('\n### Level 1 ###')
# Exercises: Level 1
# 1 Explain the difference between map, filter, and reduce.
'''Las 3 son funciones de alto orden propias de Python. Map toma una funcion y la aplica sobre un iterable, devuelve una lista con los objetos de la lista original modificados por la funcion. Filter toma como parametro una funcion que devuelve True o False, y dependiendo de eso agrega los objetos del iterable a la lista o no. Reduce tambien toma una funcion y un iterable, pero no devuelve una lista sino un solo objeto, aplica la funcion a los primeros dos elementos, luego al resultado con el siguiente objeto, y asi.'''

# 2 Explain the difference between higher order function, closure and decorator
'''Una HOF es una funcion que toma como parametro a otra funcion, o que devuelve una funcion. Closure es una variable que esta definida en el wrapper de una funcion anidada, que puede ser tambien tomada por la funcion interna. Decorator es una HOF que toma una funcion como parametro, la envuelve y modifica para dar otro resultado, pero no cambia a la funcion original. Los decoradores sirven para medir el tiempo de ejecucion de una funcion, para verificar permisos o autentificacion, para loggear funciones, para validar argumentos, etc. '''

import time

def medir_tiempo(func):
    def envoltura():
        inicio = time.time()
        func()
        fin = time.time()
        print(f"Duró {fin - inicio:.4f} segundos.")
    return envoltura

@medir_tiempo
def tarea_pesada():
    time.sleep(1)
    print("Proceso terminado.")

tarea_pesada()

# 3 Define a call function before map, filter or reduce, see examples.
def square(a):
    return a**2

numbers_squared = list(map(square, numbers))
print('#3 map:', numbers_squared)

def is_even(a):
    return a % 2 == 0

even_numbers = list(filter(is_even, numbers))
print('#3 filter:', even_numbers)

from functools import reduce

def sumar(a, b):
    return a + b

total = reduce(sumar, numbers)
print('#3 reduce:', total)

# 4 Use for loop to print each country in the countries list.
for country in countries:
    print('#4:', country)

# 5 Use for to print each name in the names list.
for name in names:
    print('#5:', name)

# 6 Use for to print each number in the numbers list.
for number in numbers:
    print('#6:', number)

print('\n### Level 2 ###')
# Exercises: Level 2
# 1 Use map to create a new list by changing each country to uppercase in the countries list
def uppercase(i):
    return i.upper()

countries_upper = list(map(uppercase, countries))
print('#1:', countries_upper)

# 2 Use map to create a new list by changing each number to its square in the numbers lis
def square(a):
    return a**2

numbers_squared = list(map(square, numbers))
print('#2:', numbers_squared)

# 3 Use map to change each name to uppercase in the names list
names_upper = list(map(uppercase, names))
print('#3:', names_upper)

# 4 Use filter to filter out countries containing 'land'.
def land_filter(i):
    return 'land' in i

countries_land = list(filter(land_filter, countries))
print('#4:', countries_land)

# 5 Use filter to filter out countries having exactly six characters.
def six_filter(i):
    return len(i) == 6

countries_six = list(filter(six_filter, countries))
print('#5:', countries_six)

# 6 Use filter to filter out countries containing six letters and more in the country list.
def six_or_more(i):
    return len(i) >= 6

countries_six = list(filter(six_or_more, countries))
print('#6:', countries_six)

# 7 Use filter to filter out countries starting with an 'E'
def is_E(i):
    return 'E' == i[0]

countries_with_E = list(filter(is_E, countries))
print('#7:', countries_with_E)

# 8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
resultado = reduce(
    lambda a, b: a + b,
    filter(
        lambda x: x > 10,
        map(
            lambda x: x * 2,
            numbers
        )
    )
)

print("#8:", resultado)

# 9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
various = ['naranja', 18, False, 'pomelo', sumar]
def get_string_lists(lt):
    return [i for i in lt if isinstance(i, str)] # isinstance es un metodo que devuelve True si el objeto es del tipo indicado
    
print('#9:', get_string_lists(various))

# 10 Use reduce to sum all the numbers in the numbers list.
total = reduce(sumar, numbers)
print('#10:', total)

# 11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def concatenate(a, b):
    return a + ' ' + b

# TODO: terminar este ejercicio

sentence = reduce(concatenate, countries)
print('#11:', sentence)

# 12 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(lt):
    pass
# TODO: terminar este ejercicio

# 13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

# TODO: terminar este ejercicio

# 14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten():
    from countries import countries as countries_all
    return countries_all[:10]
print('#14:', get_first_ten())

# 15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten():
    from countries import countries as countries_all
    return countries_all[-10:]
print('#15:', get_last_ten())

print('\n### Level 3 ###')
# Exercises: Level 3
# Use the countries_data.py file and follow the tasks below:
# Sort countries by name, by capital, by population
# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.