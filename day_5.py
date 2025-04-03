# 1 Declare an empty list
list1 = []

# 2 Declare a list with more than 5 items
list2 = ['yerba', 'café', 'te', 'leche', 'azúcar', 'canela', 'cacao']

# 3 Find the length of your list
print(len(list1)) # 0
print(len(list2)) # 6

# 4 Get the first item, the middle item and the last item of the list
print(list2[0], list2[3], list2[-1]) # yerba leche cacao

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Gabriel', 31, 1.83, True, 'Gascón']

# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7 Print the list using print()
print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 8 Print the number of companies in the list
print(len(it_companies)) # 7 

# 9 Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[-1]) # Facebook Apple Amazon

# 10 Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies) # ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 11 Add an IT company to it_companies
it_companies.append('Mercado Libre')
print(it_companies) # ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Mercado Libre']

# 12 Insert an IT company in the middle of the companies list
middle = int(len(it_companies) / 2)
it_companies.insert(middle, 'Globant')
print(it_companies) # ['Meta', 'Google', 'Microsoft', 'Apple', 'Globant', 'IBM', 'Oracle', 'Amazon', 'Mercado Libre']

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies) # ['META', 'Google', 'Microsoft', 'Apple', 'Globant', 'IBM', 'Oracle', 'Amazon', 'Mercado Libre']

# me confundí y primero lo hice para todos los nombres:
it_companies_str = ', '.join(it_companies)
it_companies_str = it_companies_str.upper()
it_companies_upper = it_companies_str.split(', ')
print(it_companies_upper) # ['META', 'GOOGLE', 'MICROSOFT', 'APPLE', 'GLOBANT', 'IBM', 'ORACLE', 'AMAZON', 'MERCADO LIBRE']

# 14 Join the it_companies with a string '#;  '
it_companies_str = '#;  '.join(it_companies)
print(it_companies_str)

# 15 Check if a certain company exists in the it_companies list.
print('Google' in it_companies) # True
print('Open IA' in it_companies) # False

# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies) # ['Amazon', 'Apple', 'Globant', 'Google', 'IBM', 'META', 'Mercado Libre', 'Microsoft', 'Oracle']

# 17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies) # ['Oracle', 'Microsoft', 'Mercado Libre', 'META', 'IBM', 'Google', 'Globant', 'Apple', 'Amazon']

# 18 Slice out the first 3 companies from the list
it_companies_sliced = it_companies[:3]
print(it_companies_sliced) # ['Oracle', 'Microsoft', 'Mercado Libre']

# 19 Slice out the last 3 companies from the list
it_companies_sliced = it_companies[-3:]
print(it_companies_sliced) # ['Globant', 'Apple', 'Amazon']

# 20 Slice out the middle IT company or companies from the list
middle = len(it_companies) // 2
middle_company = it_companies[middle]
print(middle_company ) # IBM

# 21 Remove the first IT company from the list
it_companies.pop(0)
print(it_companies) # ['Microsoft', 'Mercado Libre', 'META', 'IBM', 'Google', 'Globant', 'Apple', 'Amazon']

# 22 Remove the middle IT company or companies from the list
middle = len(it_companies) // 2 
del it_companies[middle]
print(it_companies) # Borra el 5: ['Microsoft', 'Mercado Libre', 'META', 'IBM', 'Globant', 'Apple', 'Amazon'] 

# 23 Remove the last IT company from the list
it_companies.pop()
print(it_companies) # ['Microsoft', 'Mercado Libre', 'META', 'IBM', 'Globant', 'Apple']

# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies) # []

# 25 Destroy the IT companies list
del it_companies
# print(it_companies) da error

# 26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
all_courses = front_end + back_end
print(all_courses) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = all_courses.copy()
index = full_stack.index('Redux')
full_stack.insert(index, 'Python')
full_stack.insert(index + 1, 'SQL')
print(full_stack) # ['HTML', 'CSS', 'JS', 'React', 'Python', 'SQL', 'Redux', 'Node', 'Express', 'MongoDB']

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print('Min: ', ages[0], '. Max: ', ages[-1]) # Min:  19 . Max:  26

# Add the min age and the max age again to the list
min = ages[0]
max = ages[-1]
ages.append(ages[0]) # esto funciona
ages.append(max)
ages.sort()
print(ages) # [19, 19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 26]

# Find the median age (one middle item or two middle items divided by two)
print(len(ages) % 2 == 0) # True. Es par, así que tomo los dos del medio y divido
index = len(ages) // 2
median = (ages[index] + ages[index + 1]) / 2
print(median) # 24.0

# Find the average age (sum of all items divided by their number )
average = (ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8] + ages[9] + ages[10] + ages[11] ) / len(ages)
print(average) # 22.75

average = sum(ages) / len(ages)
print(average)# 22.75

# Find the range of the ages (max minus min)
range = ages[-1] - ages[0]
print('Range is: ', range) # 7

# Compare the value of (min - average) and (max - average), use abs() method
# The abs() function returns the absolute value of the specified number.
abs_min = abs(min - average)
abs_max = abs(max - average)
print(abs_min == abs_max) # False
print(abs_min < abs_max) # False
print(abs_min > abs_max) # True

# 1 Find the middle country(ies) in the countries list

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(len(countries) % 2 == 0) # False, es impar.
index = len(countries) // 2
print(countries[index]) #Lesotho 

# 2 Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[:index + 1]
second_half = countries[index + 1:]
print(first_half[0], first_half[-1]) # Afghanistan Lesotho
print(second_half[0], second_half[-1]) # Liberia Zimbabwe

# 3 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic_countries = countries
print(ch) # China
print(ru) # Russia
print(us) # USA
print(scandic_countries) # ['Finland', 'Sweden', 'Norway', 'Denmark']

