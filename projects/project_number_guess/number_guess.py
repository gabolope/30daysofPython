# The objective of this project is to build a simple number guessing game that challenges the user to identify a randomly selected number within a specified range. The game begins by allowing the user to define a range by entering a lower and an upper bound (for example, from A to B). Once the range is set, the system randomly selects an integer that falls within this user-defined interval. The user's task is then to guess the chosen number using as few attempts as possible. The game provides feedback after each guess, helping the user refine their next guess based on whether their previous attempt was too high or too low.
import random

print('Bienvenido al juego de adivinacion de numeros.\nUsted elegira un numero y minimo y maximo, el sistema va a elegir un numero al azar dentro de ese rango y usted tendra que adivinar cual es.\n')
""" 

min_user = int(input('Ingrese el numero minimo: '))
max_user = int(input('Ingrese el numero maximo: '))
   
user_tries = 0

if isinstance(min_user, int) and isinstance(max_user, int):
    if max_user > min_user:
        secret_number = random.randint(min_user, max_user)
        print(secret_number)
        user_guess = int(input('Ingrese su respuesta: '))
        if isinstance(user_guess, int):
            while user_guess != secret_number:
                if max_user >= user_guess >= min_user:
                    if user_guess > secret_number:
                        print('Muy alto')
                        user_tries += 1
                    elif user_guess < secret_number:
                        print('Muy bajo.')    
                        user_tries += 1
                else:
                    print('La respuesta no esta en el rango.')
                user_guess = int(input('Ingrese nuevamente su respuesta: '))
            else:  
                print(f'Acertaste!\nNumero de intentos: {user_tries}')
        else:
            print('La respuesta no es un numero entero.')
    else:
        print('El maximo es menor que el minimo.')
else:
    print('El minimo o maximo no corresponde a un numero entero.') 
 """

while True:
    try:
        min_user = int(input('Ingresa el numero minimo: '))
        max_user = int(input('Ingresa el numero maximo: '))
        if max_user > min_user:
            break
        else:
            print('El maximo es menor que el minimo, intenta de vuelta.')
    except ValueError:
        print('No ingresaste numeros enteros')

secret_number = random.randint(min_user, max_user)
user_tries = 0

while True:
    try:
        user_number = int(input('Adivina: '))
        if max_user >= user_number >= min_user:
            user_tries += 1
            if user_number > secret_number:
                print('Muy alto. Intenta de nuevo.')
            elif user_number < secret_number:
                print('Muy bajo. Intenta de nuevo.')
            else:
                print(f'Acertaste!\nNumero de intentos: {user_tries}')
                break
        else:
            print('La respuesta no esta en el rango que indicaste.')
    except ValueError:
        print('No ingresaste un numero entero')