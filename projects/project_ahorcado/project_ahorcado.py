import random
import string

word_list = ['maNzana', 'Banana', 'Pera']
letters = list(string.ascii_lowercase)

word = random.choice(word_list).lower()
word_total = word

for letter in word:
    word = word.replace(letter, '_ ')
print(word)
print(word_total)

print(f'Adivina la palabra:\n{word}')



while True:
    try:
        response = input('Ingresa una letra: ').lower()
        if len(response) == 1:
            if response in word:
                pass
        else:
            print('Ingresa una unica letra')
    except ValueError:
        print('No ingresaste una letra.')
