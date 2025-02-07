import random
import math
import sys

random_number = math.ceil(random.random() * 10)

permission_error = "Please enter a valid number, either 1 or 0."
difficulty_error = "Please enter a valid number, either 1, 2 or 3."


def difficultyName(level):
    if level == 1:
        return "Easy"
    elif level == 2:
        return "Normal"
    elif level == 3:
        return "Hard"


def chooseDifficulty():
    while True:
        try:
            print(
                "Enter 1 for Easy (7 Chances)\n"
                "Enter 2 for Normal (5 Chances)\n"
                "Enter 3 for Hard (3 Chances)\n"
            )
            difficultyLevel = int(input())
        except ValueError:
            print(difficulty_error)
            continue

        if difficultyLevel not in [1, 2, 3]:
            print(difficulty_error)
            continue
        else:
            return difficultyLevel


def totalChances(chosen_difficulty):
    if chosen_difficulty == "Easy":
        return 7
    elif chosen_difficulty == "Normal":
        return 5
    elif chosen_difficulty == "Hard":
        return 3


def checkNumber(chosen_difficulty):
    difficulty_level_name = difficultyName(chosen_difficulty)
    chances = totalChances(difficulty_level_name)
    print(
        f"Now let's play the game as you have chosen the {difficulty_level_name} level. "
        f"You will get a total of {chances} chances."
    )

    while chances:
        try:
            userInput = int(input("Enter the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if userInput == random_number:
            print("Congratulations! You guessed it!")
            break
        else:
            chances -= 1
            if chances > 0:
                print(f"Incorrect guess. You have {chances} chances remaining.")
            else:
                print("Sorry, you've used all your chances. Better luck next time!")
                break


print("A random number has been generated between 1 and 10.\n")

while True:
    try:
        user_choice = int(
            input(
                "If you want to play the 'Guess the Random Number' game, enter 1. "
                "If not, enter 0: "
            )
        )
    except ValueError:
        print(permission_error)
        continue

    if user_choice not in [0, 1]:
        print(permission_error)
    elif user_choice == 0:
        sys.exit()
    elif user_choice == 1:
        print(
            "\nNow let's play the game\n"
            "First, please choose the difficulty level. You will get the number of chances according to the difficulty level you choose."
        )
        chosen_difficulty = chooseDifficulty()
        checkNumber(chosen_difficulty)
        break
