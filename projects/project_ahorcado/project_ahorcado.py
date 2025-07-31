import requests
import string
from unidecode import unidecode

url = 'https://random-word-api.herokuapp.com/word?lang=es'
word = requests.get(url).json()[0]

word_len = len(word) 
letters = list(string.ascii_lowercase)
tries = word_len + 4
placeholder = ''.join(['_ '] * word_len)
responses = list()

print(f'Adivina la palabra:\n{placeholder}\n')

while True:
    try:
        response = input('Ingresa una letra: ').lower()
        if len(response) == 1:
            if response in letters:
                letters.remove(response)
                responses.append(response)
                placeholder = ''.join(f'{c} ' if unidecode(c) in responses else '_ 'for c in word)
                print(placeholder)
                print(f'Respuestas: {responses}')
                tries -= 1
                if '_' not in placeholder:
                    print(f'Acertaste!!!\nLa palabra era ¨{word}¨\n')
                    break
                print(f'Intentos restantes: {tries}')
                if tries == 0:
                    print(f'Te quedaste sin intentos. Perdiste.\nLa palabra era ¨{word}¨\n')
                    break
            else:
                print('Ya probaste con esa letra.')
                print(f'Intentos restantes: {tries}\n')
        else:
            if unidecode(response) == unidecode(word):
                print(f'Acertaste!!!\nLa palabra era ¨{word}¨\n')
                break
            else:
                print('La palabra es incorrecta. ')
                tries -= 1
                print(f'Intentos restantes: {tries}')
                if tries == 0:
                    print(f'Te quedaste sin intentos. Perdiste.\nLa palabra era ¨{word}¨\n')
                    break
    except ValueError:
        print('No ingresaste una letra. \n')
