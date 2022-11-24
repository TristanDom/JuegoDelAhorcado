"""
Hangman es un programa el cual está basado en el típico juego del ahorcado 
el cual pone a prueba tu léxico y memoria para poder jugar.
Este programa está creado por Tristán Domínguez
https://github.com/TristanDom
"""


# Importa las funciones random para la elección de palabras.
import random
# Importa la lista palabras del módulo Palabras las cuales están en inglés.
from Palabras import words
# Importa la funció string para conocer los valores ingresados por teclado y convertirlos en mayúscula.
import string
# Importa la lista de palabras del módulo words las cuales están en español.
from Words import palabras


# Funció para obtener una palabra válida.
def get_valid_word(lengua):  
    # Escoge un palabra rándom con la función random de la lista de palabras.
    word = random.choice(lengua)
    # Mientras que en la palabra seleccionada haya un guión o un espacio vacío ejecuta.
    while '-' in word or ' ' in word:
        # Escoge un palabra rándom con la función random de la lista de palabras.
        word = random.choice(lengua)
    # Retorna la palabra seleccionada aleatoreamente y la convierte en mayúscula.
    return (word.upper())


def select_lenguage():
    print("Selecciona el lenguaje con el que desees jugar.")
    lenguag = input(
        "Digita la letra 'E' si deseas jugar en español y la letra 'I' si deseas jugar en inglés: ")
    lenguage = lenguag.upper()
    while (lenguage != "E") or (lenguage != "I"):
        if lenguage == "E":
            print("Haz seleccionado el idioma español.")
            return (palabras)
        elif lenguage == "I":
            print("Haz seleccionado el idioma inglés.")
            return (words)
        else:
            print("Por favor intruduce un elemento válido!")
            lenguag = input(
                "Digita la letra 'E' si deseas jugar en español y la letra 'I' si deseas jugar en inglés: ")
            lenguage = lenguag.upper()


def live():
    print("selecciona la dificultad con la que deseas torturarte: ")
    lives_t = input("Bebé (B), Homo sapiens (H) o Erudito (E): ")
    liv = lives_t.upper()
    while (liv != "B") or (liv != "H") or (liv != "E"):
        if (liv == "B"):
            print("Muy bien bebé, vamos a jugar.")
            return (15)
        elif (liv == "H"):
            print("Muy bien homo sapiens, vamos a jugar.")
            return (7)
        elif (liv == "E"):
            print("Wow, tanto crees en ti?, vamos a comprobarlo ;)")
            return (3)
        else:
            print("Selecciona una dificultad válida, no es tan difícil.")
            lives_t = input("Bebé (B), Homo sapiens (H) o Erudito (E): ")
            liv = lives_t.upper()


def hangman():  # Función hangman que ejecuta todo y la llama la función get_valid_word.
    lengua = select_lenguage()
    # Almacena en la variable word la palabra seleccionada en la función get_valid_word.
    word = get_valid_word(lengua)
    word_letters = set(word)  # Convierte la variable word en objeto.
    # Almacena en una variable los valores ascii en mayúscula.
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Crea un objeto vacío.
    lives = live()
    # Mientras que la distancia del objeto word_letters sea mayor a cero.
    while len(word_letters) > 0 and lives > 0:
        # Si la palabra usada ya se ha usado se agrega al objeto used_letters.
        print('Haz usado las letras: ', ' '.join(used_letters))
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print('Tienes: ', lives, 'vidas. ')
        print('Letra actual: ', ' '.join(word_list))
        user_letter = input("Adivina una letra: ").upper()
        if (user_letter in alphabet - used_letters):
            used_letters.add(user_letter)
            if (user_letter in word_letters):
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # Toma una vida cada respuesta errónea.
                print('La letra no está en la palabra.')
        elif (user_letter in used_letters):
            print("Ya haz usado esta letra, intenta de nuevo: ")
        else:
            print("Caracter inválido, intenta de nuevo, no es tan dificil: ")
    if lives == 0:
        print("Perdedor@, la palabra era: ", word)
    else:
        print("Muy bien, no eres tan inútil, la palabra es: ", word, "!!!")


hangman()
