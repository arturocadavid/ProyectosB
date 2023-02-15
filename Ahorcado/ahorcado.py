import random
import time

# Pasos iniciales para empezar el juego:
print("\n¡Bienvenido al juego del Ahorcado!\n")
name = input("Ingresa tu nombre: ")
print("Hola ¡" + name + "! ¡Mucha suerte!")
time.sleep(2)
print("El juego iniciará\n ¡Juguemos al ahorcado!")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["camion","cama","trompeta","libro","experimento","completo","magia","intentar","veneno","feliz","arbol"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    
# Un bucle para volver a ejecutar el juego cuando termina la primera ronda:
def play_loop():
    global play_game
    play_game = input("¿Quieres jugar de nuevo? y = si, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("¿Quieres jugar de nuevo? y = si, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("¡Gracias por jugar! Hecho por: Arturo Cadavid")
        exit()
        
# Condiciones requeridas para el juego:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Esta es la palabra: " + display + " Ingresa una letra: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Error, intenta con una letra\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Intenta otra letra.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Letra equivocada. " + str(limit - count) + " intentos restantes:\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Letra equivocada. " + str(limit - count) + " intentos restantes:\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Letra equivocada. " + str(limit - count) + " intentos restantes:\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Letra equivocada. " + str(limit - count) + " intentos restantes:\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Letra equivocada. ¡¡¡Te has ahorcado!!!\n")
            print("La palabra era:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("¡Felicitaciones! ¡Has adivinado la palabra!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()