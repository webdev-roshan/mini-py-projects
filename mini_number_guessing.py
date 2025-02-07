import random
import math


random_number = math.ceil(random.random() * 10)
print(random_number)


try:
    user_input = int(
        input(
            "A Random Number has been generated between 1 - 10 \nGuess the number and win prizes \n"
        )
    )
except ValueError:
    print("Enter a proper number")


if user_input == random_number and user_input <= 10:
    print("Correct Guess")
elif user_input > 10:
    print("Pleae Enter the number between 1 - 10")
else:
    print("Enter a correct number")
