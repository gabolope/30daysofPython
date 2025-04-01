# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty ' + 'Days ' + 'Of ' + 'Python.')

# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4 Print the variable company using print().
print(company)

# 5 Print the length of the company string using len() method and print().
company_lenght = len(company)
print(company_lenght)

# 6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 Cut(slice) out the first word of Coding For All string.
print(company[6:company_lenght])

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding') != -1)

# 11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12 Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace('All', 'Everyone'))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

# 15 What is the character at index 0 in the string Coding For All.
print(company[0])   

# 16 What is the last index of the string Coding For All.
print(company[-1])

# 17 What character is at index 10 in "Coding For All" string.
print(company[10])

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(company[0]+company[7]+company[11])

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

# 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
initial = sentence.index('because')
final = sentence.rindex('because') + len('because')
print(sentence[0:initial] + sentence[final:len(sentence)])

# 26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# 27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# 28 Does 'Coding For All' start with a substring Coding?
index = company.index('Coding')
print(index == 0)

# 29 Does 'Coding For All' end with a substring coding?
index = company.rindex('Coding')
print(index == (len(company) - len('Coding')))

# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
company = '   Coding For All      '
print(company.strip())

# 31 Which one of the following variables return True when we use the method isidentifier():
#    30DaysOfPython
#    thirty_days_of_python

# 32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# 33 Use the new line escape sequence to separate the following sentences
#    I am enjoying this challenge.
#    I just wonder what is next.
sentence_1 = 'I am enjoying this challenge.'
sentence_2 = 'I just wonder what is next.'
print(sentence_1)