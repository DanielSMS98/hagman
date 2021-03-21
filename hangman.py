from colorama import Fore, Back, Style, init
from words import palabras
import random
init()

print("Bienvenido al juego del ahorcado")

def get_valid_palabra(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra

mi_palabra = get_valid_palabra(palabras)
espacios_vacios = mi_palabra+'\n',len(mi_palabra)

print( Fore.RED +"-"*len(mi_palabra))
