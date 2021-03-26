#from colorama import Fore, Back, Style, init
from words import palabras
import random
import string
from drawing import hangman_drawing
#init()


#Metodo de iniciacion del progrma indica el inicio y pregunta si quieres jugar
def main():
    cont = 0
    while(cont == 0 ):
        print("Bienvenido al juego del ahorcado")
        cont = int(input("¿Deseas jugar?\n[1]Si\n[2]No\n"))        
        if(cont == 1):
            hangman()
            cont = 0
        elif(cont == 2):
            print("\nAdios")
            exit()
        else:
            print("\nIntroduccion erronea, vuelve a introducirlo\n")
            cont = 0
            

#Metod para selecionar la palabra en lo cual la sacara de la lista
#del documneto "words"
def get_valid_palabra(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra.upper()


#Juego del ahorcado
def hangman():
    mi_palabra = get_valid_palabra(palabras)
    palabra_separada = list(mi_palabra)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    drawing = 0
    lives = 6

    while len(palabra_separada) > 0 and lives > 0:
        print(hangman_drawing[drawing])
        print("Intentos: ",lives)
        word_list = [letter if letter in used_letter else '-' for letter in mi_palabra]
        print('Palabra: ',' '.join(word_list))
        user_letter = input('Introduce una letra: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in palabra_separada:        
                palabra_separada.remove(user_letter)
            else:
                lives = lives - 1
                drawing = drawing + 1
        elif user_letter in used_letter:
            print("Repetiste una letra")
        else:
            print("Caracter invalido")
    if(lives > 0):
        print(f"\nTu palabra era {mi_palabra}\nGanaste\n")
    else:
        print(f"\nTu palabra era {mi_palabra}\nPerdistes\n")


main()