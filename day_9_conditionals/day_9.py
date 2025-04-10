# Exercises: Level 1
# 1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    print('You need', (18 - age), 'more years to drive.')

# 2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
my_age = 31
if my_age > age:
    if abs(my_age - age) > 1:
        print('I am', my_age - age, 'years older than you.' )
    else: 
        print('I am', my_age - age, 'year older than you.' )
elif age > my_age:
    if abs(age - my_age) > 1:
        print('You are', age - my_age, 'years older than you.' )
    else: 
        print('You are', age - my_age, 'year older than you.' )
else:
    print('We are the same age.')

# 3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 
num1 = float(input('Enter number A: '))
num2 = float(input('Enter number B: '))
if num1 > num2:
    print('A is greater than B.')
elif num1 < num2:
    print('A is smaller than B.')
else:
    print('A is equal to B.')

# Exercises: Level 2
# 1 Write a code which gives grade to students according to theirs scores:
""" 
    80-100, A
    70-89, B
    60-69, C
    50-59, D
    0-49, F 
"""
score = int(input('Enter the student score: '))
if score < 0 or score > 100:
    print('You did not enter a number between 0 and 100.')
elif score >= 80:
    print('The student got an A.')
elif score >= 70:
    print('The student got a B.')
elif score >= 60:
    print('The student got a C.')
elif score >= 50:
    print('The student got a D.')
else:
    print('The student got a F.')

# 2 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = str(input('Enter the current month: ')).lower()
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

if month not in months:
    print('You did not enter a correct month.')
elif month == 'december' or month == 'january' or month == 'february':
    print('It is summer!')
elif month == 'march' or month == 'april' or month == 'may':
    print('It is autumn!')
elif month == 'june' or month == 'july' or month == 'august':
    print('It is winter!')
else:
    print('It is spring!')

# 3 The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('Enter a fruit: ').lower())

if fruit in fruits:
    print('That fruit already exists in the list.')
else:
    fruits.append(fruit)
    print(fruits)

# Exercises: Level 3
# 1 Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person :
    middle = len(person['skills']) // 2
    skills = person['skills']
    print(skills[middle])
else:
    print('This person does not have skills key.')

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person['skills']:
    print('This person knows Python!')
else:
    print('This does not know Python.')

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
skills_set = set(person['skills']) # lo paso a set para que el orden en el que están las skills no afecte
if {'JavaScript','React'} == skills_set:
    print('The person is a front end developer.')
elif {'Node','Python', 'MongoDB'} == skills_set:
    print('The person is back end developer.')
elif {'React','Node', 'MongoDB'} == skills_set:
    print('The person is fullstack developer.')
else:
    print('Unkown title.')

# If the person is married and if he lives in Finland, print the information in the following format:  Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] == True and person['country'] == 'Finland':
    print(person['first_name'], person['last_name'], 'is married and he lives in', person['country'])
else:
    print('ni idea bo')
