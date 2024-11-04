
import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# selecciona una palabra random de la lista "someWords" .
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        # para imprimir los espacios en blanco
        print('_', end=' ')
    print()

    playing = True
    # guarda las letras que adivina el jugador
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:  # Flag se actualiza cuando la palabra es adivinada correctamente
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validación de la suposición
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # Si la letra es adivinada correctamente
            if guess in word:
                # k almacena el número de veces que la letra adivinada ocurre en la palabra
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # La letra adivinada se agrega tantas veces como ocurre

            # Imprime la palabra
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # Si el usuario ha adivinado todas las letras
                # Una vez que se adivina completamente la palabra correcta,
                elif (Counter(letterGuessed) == Counter(word)):
                    # el juego termina, incluso si quedan oportunidades
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # Para romper el bucle for
                    break  # Para romper el bucle while
                else:
                    print('_', end=' ')

        # Si el usuario ha usado todas sus oportunidades
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()