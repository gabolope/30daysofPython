# 1 Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import requests
import collections
import re

url = 'http://www.gutenberg.org/files/1112/1112.txt'
url2 = 'https://folger-main-site-assets.s3.amazonaws.com/uploads/2022/11/romeo-and-juliet_TXT_FolgerShakespeare.txt'

response = requests.get(url)
print(response.status_code) # da 404 porque no se encuentra
response = requests.get(url2)
print(response.status_code) # da 200 porque esta OK

text = response.text

def find_most_common_words(txt, int):
    text_lower = txt.lower()
    word_list = re.findall(r'\b[a-zA-Z]+\b', text_lower) # toma los limites de las palabras y solo las letras.  
    word_count = collections.Counter(word_list)
    word_common = word_count.most_common(int)
    return word_common

print('#1:', find_most_common_words(text, 10))

# 2 Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats

cats_url = 'https://api.thecatapi.com/v1/breeds'

cats_response = requests.get(cats_url)
cats_api = cats_response.json()

weight_list_raw = []
for breed in cats_api:
    weight_list_raw.append(breed['weight']['metric'])

weight_list = []
for string_range in weight_list_raw:
    min_weight = int(string_range[0])
    max_weight = int(string_range[-1])
    num_range = list(range(min_weight, max_weight + 1))
    weight_list.extend(num_range)

import statistics
print('Peso minimo:', min(weight_list)) # 2
print('Peso maximo:', max(weight_list)) # 9
print('Promedio:', statistics.mean(weight_list)) #4.77
print('Media:', statistics.median(weight_list)) #5
print('Desviacion estandar:', statistics.stdev(weight_list)) #1.56



# 3 Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API

# 4 UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
