# Exercises: Level 1
print('### Level 1 ###')
# 1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b
print('#1:', add_two_numbers(4, 4))

# 2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def  area_of_circle(r):
    area = r * r * 3.14
    return area
print('#2:', area_of_circle(3))

# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*num):
    count = 0
    for i in num:
        count += i
    return count
print('#3:', add_all_nums(1, 1, 1, 1, 1))

# 4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_c_to_f(c):
    return (c * 9/5) + 32
print('#4:', convert_c_to_f(0))

# 5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month_str = str(month).lower()
    match month_str:   # uso switch case para probar
        case 'december' | 'january' | 'february':
            return 'Summer'
        case 'march' | 'april' | 'may':
            return 'Autumn'
        case 'june' | 'july' | 'august':
            return 'Winter'
        case 'september' | 'october' | 'november':
            return 'Spring'
        case _:       # el símbolo _ toma los casos restantes
            return 'Invalid month'
print('#5:', check_season('october'))

# 6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return(slope)
print('#6:', calculate_slope(1, 2, 3, 4))

# 7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    x = ((c / b) ** 1/2) / a
    return x
print('#7:', solve_quadratic_eqn(1, 2, 3))

# 8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
print('#8: ')
def print_list(lt):
    for i in lt:
        print(i) 

fruits  = ['banana', 'manzana', 'pera']
print_list(fruits)

# 9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lt):
    lt_reverse = list()
    for i in lt:
        lt_reverse.insert(0, i)
    return lt_reverse
print('#9:', reverse_list(fruits))

# 10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lt):
    lt_cap = list()
    for i in lt:
      lt_cap.append(i.capitalize())  
    return lt_cap
print('#10:', capitalize_list_items(fruits))

# 11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.