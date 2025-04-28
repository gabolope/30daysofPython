print('\n### Level 1 ###')
# Exercises: Level 1
# 1 Write a function which generates a six digit/character random_user_id
from random import choice, randint, shuffle, sample
from string import ascii_letters as letters, digits as numbers

alphanumeric = letters + numbers
def random_user_id():
    id = ''
    count = 0
    while count < 6:
        id += choice(alphanumeric)
        count += 1
    return id

def random_user_id(): # hecha por el CHAT 
    return ''.join(choice(alphanumeric) for _ in range(6)) # el _ se usa como una variable descartable, cuando no vas a usar su valor. 

print('#1:', random_user_id())

# 2 Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_characters = int(input('Enter number of characters: '))
    num_ids = int(input('Enter number of IDs: '))
    ids = list()
    for _ in range(num_ids):
        new_id = ''
        for _ in range(num_characters):
            new_id += choice(alphanumeric)
        ids.append(new_id)
    for i in ids:
        print('#2:', i)


# 3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    color = list()
    for _ in range(3):
        color.append(randint(0, 255))
    return color

print('#3:', rgb_color_gen())

print('\n### Level 2 ###')
# Exercises: Level 2
# 1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num):
    f_index = letters.find('f')
    hexa = numbers + letters[:f_index + 1]
    color_lt = list()
    for _ in range(num):
        color = '#'
        for _ in range(6):
            color += choice(hexa)
        color_lt.append(color)
    return color_lt

print('#1:', list_of_hexa_colors(3))

# 2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
    color_lt = list()
    for _ in range(num):
        color = ''
        for _ in range(3):
            if len(color) == 0:
                color += str(randint(0, 255))
            else: 
                color += ', ' + str(randint(0, 255))
        color_lt.append(color)
    return color_lt

print('#2:', list_of_rgb_colors(2))

# 3 Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type, num): 
    color_lt = list()
    f_index = letters.find('f')
    hexa = numbers + letters[:f_index + 1]
    if type == 'rgb':
        for _ in range(num):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            rgb_color = f'rgb({r}, {g}, {b})'
            color_lt.append(rgb_color)
        return color_lt
    elif type == 'hexa':
        for _ in range(num):
            color = '#'
            for _ in range(6):
                color += choice(hexa)
            color_lt.append(color)
        return color_lt
    else:
        return 'Type of color is not valid.'

print('#3:', generate_colors('rgb', 3))
print('#3:', generate_colors('hexa', 3))

print('\n### Level 3 ###')
# Exercises: Level 3 
# 1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

def shuffle_list(lt):
    shuffled_lt = list()
    for i in lt:
        shuffled_lt.insert(choice(range(10)), i)
    return shuffled_lt

def shuffle_list2(lt):
    shuffle(lt)
    return lt

print('#1:', shuffle_list(days))
print('#1:', shuffle_list2(days))

# 2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def random_numbers():
    nums = list(range(10))
    shuffle(nums)
    return nums[:7]

def randon_numbers():
    return sample(range(10), 7)
print('#2:', random_numbers())