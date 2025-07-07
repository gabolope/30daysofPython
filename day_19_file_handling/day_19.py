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
import os

def find_most_common_words(path, int):
    if os.path.isfile(path):
        with open(path, encoding='utf-8') as f:
            text = f.read()
    else:
        text = path
    text_lower = text.lower()
    word_list = re.findall(r'\b[a-zA-Z]+\b', text_lower) # toma los limites de las palabras y solo las letras.  
    word_count = Counter(word_list)
    word_common = word_count.most_common(int)
    return word_common


# 6 Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
print('#6 Obama:', find_most_common_words('./day_19_file_handling/obama_speech.txt', 10))
print('#6 Trump:', find_most_common_words('./day_19_file_handling/donald_speech.txt', 10))
print('#6 Michelle:', find_most_common_words('./day_19_file_handling/michelle_obama_speech.txt', 10))
print('#6 Melina:', find_most_common_words('./day_19_file_handling/melina_trump_speech.txt', 10))
print('#6 Otro texto:', find_most_common_words('Hay que hacer lo que hay que hacer porque el hacer es lo que dicta lo que hay', 10))


# 7 Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

def clean_text(path1, path2):
    # checkear si los dos textos son archivos o variables
    if os.path.isfile(path1):
        with open(path1, encoding='utf-8') as f:
            text1 = f.read()
    else:
        text1 = path1
    if os.path.isfile(path2):
        with open(path2, encoding='utf-8') as f:
            text2 = f.read()
    else:
        text2 = path2
    # pasar a minuscula y quedarse solo con las palabras
    text1_lower = text1.lower()
    text2_lower = text2.lower()
    word_list1 = re.findall(r'\b[a-z]+\b', text1_lower)
    word_list2 = re.findall(r'\b[a-z]+\b', text2_lower)
    return word_list1, word_list2


def remove_support_words(wl1, wl2):
    from stop_words import stop_words
    cl1 = [word for word in wl1 if word not in stop_words]
    cl2 = list(filter(lambda word: word not in stop_words, wl2))
    return cl1, cl2


def check_text_similarity(list1, list2):
    # fijarse cual tiene mayor variedad de palabras
    set1 = set(list1)
    set2 = set(list2)
    if len(set1) > len(set2):
        print('El primer texto tiene mayor variedad de palabras')
    elif len(set1) < len(set2):
        print('El segundo texto tiene mayor variedad de palabras')
    else:
        print('Ambos textos tienen la misma cantidad de variedad de palabras.')
    # calcular el indice de jaccard
    # es el largo de la interseccion de las dos listas, dividido por el largo de la union de las dos listas
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    print(f'El índice de Jaccard es: {len(intersection) / len(union)}')

# Ejecuto la aplicación:  
obama, trump = clean_text('./day_19_file_handling/obama_speech.txt', './day_19_file_handling/donald_speech.txt')
obama, trump = remove_support_words(obama, trump)
check_text_similarity(obama, trump)

# 8 Find the 10 most repeated words in the romeo_and_juliet.txt
print('#8', find_most_common_words('./day_19_file_handling/romeo_and_juliet.txt', 10))

# 9 Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
import csv
with open('./day_19_file_handling/hacker_news.csv', encoding='utf-8') as file:
    news = csv.reader(file, delimiter=',')
    line_count = 0
    python = 0
    Python = 0
    javascript = 0
    Javascript = 0
    JavaScript = 0
    Java = 0
    for row in news:
        if line_count == 0:
            line_count += 1
        else:
            if 'python' in row[1]:
                python += 1
            if 'Python' in row[1]:
                Python += 1
            if 'javascript' in row[1]:
                javascript += 1
            if 'Javascript' in row[1]:
                Javascript += 1
            if 'JavaScript' in row[1]:
                JavaScript += 1
            if 'Java' in row[1] and 'JavaScript' not in row[1]:
                Java += 1
            line_count += 1
    print('python:', python)
    print('Python:', Python)
    print('javascript:', javascript)
    print('Javascript:', Javascript)
    print('JavaScript:', JavaScript)
    print('Java but not JavaScript:', Java)
    