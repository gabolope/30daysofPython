print('\n### Level 1 ###')
# Exercises: Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

def text_counter(text):
    content = text.read()
    words = len(content)
    lines = len(content.splitlines())
    return (words, lines)

michelle = open('./day_19_file_handling/michelle_obama_speech.txt')
donald = open('./day_19_file_handling/donald_speech.txt')
melina = open('./day_19_file_handling/melina_trump_speech.txt')

with open('./day_19_file_handling/obama_speech.txt') as obama:
    print('#1: Obama Words and Lines', text_counter(obama))
with open('./day_19_file_handling/michelle_obama_speech.txt') as michelle:
    print('#1: Michelle Words and Lines', text_counter(michelle))
with open('./day_19_file_handling/donald_speech.txt') as donald:
    print('#1: Trump Words and Lines', text_counter(donald))
with open('./day_19_file_handling/melina_trump_speech.txt') as melina:
    print('#1: Melina Words and lines', text_counter(melina))

# 2 Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
from collections import Counter

def most_spoken(path, num):
    with open(path, encoding='utf-8') as file:
        language_list = []
        data_dict = json.load(file)  # load es para archivo y loads es para strings
        for i in data_dict:
            language_list.extend(i['languages']) # junta todos los idiomas en una lista
        language_count = Counter(language_list)
        language_sorted = language_count.most_common(num)
        return language_sorted

print('#2:', most_spoken('./day_19_file_handling/countries_data.json', 3))

# 3 Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated(path, num):
    with open(path, encoding='utf-8') as file:
        data_dict = json.load(file)
        data_sorted = sorted(data_dict, key= lambda x: x['population'], reverse= True)
        countries_list = []
        for dict in data_sorted[:num]:
            countries_list.append({'country': dict['name'], 'population': dict['population']})
        return countries_list

print('#3:', most_populated('./day_19_file_handling/countries_data.json', 3))

print('\n### Level 2 ###')
# Exercises: Level 2
# 4 Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re

with open('./day_19_file_handling/email_exchanges_big.txt') as file:
    text = file.read()
    email_finder = r'From\s[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' # Toma From + email
    matches = re.findall(email_finder, text) # busco todos los que tengan el regex
    email_list = [i.replace('From ', '') for i in matches] # quito el 'From ' de los strings
    print('#4:', email_list[:10])

# 5 Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(file, int):
    pass

