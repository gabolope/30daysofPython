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
example = [{
        "name": "a",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 1,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
{
        "name": "b",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 2,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
{
        "name": "c",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 3,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    }
]

def most_spoken(lt):
    language_list = ''
    count = Counter()
    sorted_list = sorted(lt, key = lambda x: x['population'], reverse = True)
    return sorted_list

print(most_spoken(example))

with open('./day_19_file_handling/countries_data.json') as countries_data:
    pass