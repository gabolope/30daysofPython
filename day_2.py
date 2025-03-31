# Día 2: 
first_name = 'Gabriel'
last_name = 'López'
full_name = 'Gabriel López'
country = 'Argentina'
city = 'Mar del Plata'
age = 31
year = 2025
is_married = True
is_true = False
is_light_on = True
month, day, season = 'april', 'monday', 'fall'

print(type(first_name))
print(type(age))
print(type(is_married))
print(type(month))

print('Length of first name:', len(first_name),'. Length of last name:', len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = int(num_one / num_two)

print( total, diff, product, division, remainder, exp, floor_division)

radius = float(input("What is the radius of the circle?"))
area_of_circle = 3.14 * (radius ** 2)
circunference_of_circle = 3.14 * 2 * radius

print("Then, the area is ", area_of_circle, 'and its circunference is ', circunference_of_circle)
