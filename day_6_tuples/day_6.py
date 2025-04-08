# Exercises: Level 1
# 1 Create an empty tuple
tpl = tuple() # o: tpl = ()
print(tpl) 

# 2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Dana', 'Alina')
brothers = ('Marcos', 'Ivan')

# 3 Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings) # ('Marcos', 'Ivan', 'Dana', 'Alina')

# 4 How many siblings do you have?
print(len(siblings)) # 4

# 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append('Darío')
siblings.append('Lucrecia')
family_members = tuple(siblings)
print(family_members) # ('Marcos', 'Ivan', 'Dana', 'Alina', 'Darío', 'Lucrecia')

# Exercises: Level 2
# 1 Unpack siblings and parents from family_members
sib1, sib2, sib3, sib4, *parents = family_members # desempaqueta a parents en una lista y a los demas como variables sueltas. 
print(sib1) # Marcos
print(sib2) # Ivan
print(sib3) # Dana
print(sib4) # Alina
print(parents) # ['Darío', 'Lucrecia']

# 2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('banana', 'manzana', 'pera')
vegetables = ('zanahoria', 'papa', 'berenjena')
animal_products = ('leche', 'huevos', 'carne')
food_stuff_tp = fruits + vegetables + animal_products

# 3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_lt) // 2
del food_stuff_lt[middle]
print(food_stuff_lt) # ['banana', 'manzana', 'pera', 'zanahoria', 'berenjena', 'leche', 'huevos', 'carne']

# 5 Slice out the first three items and the last three items from food_staff_lt list
del food_stuff_lt[:3]
print(food_stuff_lt) # ['zanahoria', 'berenjena', 'leche', 'huevos', 'carne']
del food_stuff_lt[-3:]
print(food_stuff_lt) # ['zanahoria', 'berenjena']

# 6 Delete the food_staff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp) # da error porque ya no existe

# 7 Check if an item exists in tuple:
#   Check if 'Estonia' is a nordic country
#   Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) # False
print('Iceland' in nordic_countries) # True
