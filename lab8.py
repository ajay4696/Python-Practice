print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight ! = True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("you guessed {}. That is correct! You win!". formatguess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".formatguess))
        

