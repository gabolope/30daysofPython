# 1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives = [number for number in numbers if number <= 0]
print('#1:', negatives)

# 2 Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [number for row in list_of_lists for number in row] # no lo entiendo
print('#2:', flat_list)

# 3 Using list comprehension create the following list of tuples:
""" 
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""
lt1 = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print('#3:',lt1)

# 4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [country for tpl in countries for country in tpl ]
print('#4:', countries)

#POPE:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [[country.upper(), country[0:3].upper(), city.upper()]
                    for row in countries
                        for (country, city) in row] 

print(flattened_countries)

# 5 Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dicts = [{'country': country_city[0], 'city': country_city[1]} for country_list in countries for country_city in country_list] # hecho por chat
print('#5:', countries_dicts)

# 6 Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Barak', 'Obama')], [('Bill', 'Gates')]]
names_str = [ ]

# 7 Write a lambda function which can solve a slope or y-intercept of linear functions.
x = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
print('#7:', x(1, 2, 3, 4))