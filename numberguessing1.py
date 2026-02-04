'''
BSCIT-05-0133/2024
Masindano Masila
'''

# NUMBER GUESSING GAME 2

# make a variable and assign a winning number
winning_number = 7

# loop until the correct number is guessed
while True:
    # ask the user to guess a number
    guess = int(input("Guess the number: "))

    # check the user's guess
    if(guess == winning_number):
        print("YOU WIN")
        break
    elif(guess < winning_number):
        print("Too low")
    else:
        print("Too high")
