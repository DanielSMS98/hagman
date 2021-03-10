from words import palabras
import random

print("Bienvenido al juego del ahorcado")

def get_valid_palabra(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra

hidden_palabra = set()
for letter in get_valid_palabra(palabras):
    hidden_word.add('-')
    
