'''
BSCIT-05-0133/2024
Masindano Masila
'''

# NUMBER GUESSING

# import random to generate a random number
import random

# make a variable and assign a random winning number
winning_number = random.randint(1, 10)

# ask user to guess a number
while True:
        guess = int(input("Guess the number: "))

        # check the user's guess
        if guess == winning_number:
            print("YOU WIN")
            break
        elif guess < winning_number:
            print("Too low")
        else:
            print("Too high")
