# 1,2,3 
age = 31
height = 1.83
complex_number = 3 + 2j

# 4
triangle_base = float(input('Enter triangle base '))
triangle_height = float(input('Enter triangle height '))
triangle_area = 0.5 * triangle_base * triangle_height
print('The area of the triangle is: ', triangle_area)

# 5
side_a = float(input('Enter side A of triangle '))
side_b = float(input('Enter side B of triangle '))
side_c = float(input('Enter side C of triangle '))
triangle_perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is: ', triangle_perimeter)

# 6
rectangle_lenght = float(input('Enter rectangle lenght '))
rectangle_height = float(input('Enter rectangle height '))
rectangle_area = rectangle_lenght * rectangle_height
rectangle_perimeter = 2 * ( rectangle_height + rectangle_lenght)
print('The area of the rectangle is: ', rectangle_area, '. And its perimeter is ', rectangle_perimeter)

# 7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
circle_radius = float(input('Enter circle radius '))
circle_area = 3.14 * (circle_radius ** 2)
circle_circunference = 2 * 3.14 * circle_radius
print('The area of circle is ', circle_area, '. And its circunference is ', circle_circunference)

# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
x_value = float(input('Enter X value '))
print('The Y value is ', (2 * x_value) -2)

# 9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
eucledian = ((2-6)**2+(2-10)**2)**0.5
slope = ((10-2)/(6-2))

# 10 Compare the slopes in tasks 8 and 9.
print('Are slope and euclidian distance the same? ', eucledian == slope)

# 11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_value_2 = float(input('Enter another X value '))
y_value = (x_value_2 ** 2) + (6 * x_value_2) + 9
print('Y value is ', y_value)

# 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') != len('dragon'))

# 13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this cpurse is not full of jargon')

# 15 There is no 'on' in both dragon and python
print(not 'on' in 'python' and 'on' in 'dragon')

# 16 Find the length of the text python and convert the value to float and convert it to string
text = 'python'
text_lenght = str(float(len(text)))
print(text_lenght)

# 17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
check_number = float(input('Enter a number to check if it is even '))
print(check_number % 2 == 0)

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print((7 // 3) == int(2.7))

# 19 Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# 20 Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# 21 Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input('Enter how many hours you work '))
rate = float(input('Enter your rate '))
pay = 30 * hours * rate
print('Your monthly income is ', pay)

# 22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

# 23 Write a Python script that displays the following table
""" 
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125 
"""
