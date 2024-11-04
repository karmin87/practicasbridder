import random

# imprime las instrucciones en varias lineas 
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # toma el inpute del usuario.
    choice = int(input("Enter your choice: "))

    # bucle hasta el que usuario de una opcion.
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺: '))

    # inicializa el valor de la variable choice_name  
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # imprime el resultado
    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    # seleccion random 1 2 o 3
    comp_choice = random.randint(1, 3)

    # inicializa el valor de la variable comp_choice_name correspondiente a la seleccion.
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    # determina el ganador
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Scissors'

    # imrpime el resultado
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # pregunta al usuario para jugar nuevamente
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

# After coming out of the while loop, print thanks for playing
print("Thanks for playing!")