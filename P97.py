from random import *

number = randint(1,9)

chances = 5

guess = int(input("Guess the number"))

while chances <= 5:
    if guess == number  :
        print("Congratulations, you won!")
    if not chances > 0 :
        print("You lose, the number is", number)
    elif guess < number :
        print("Your guess is too low, guess a number higher than", guess)
        guess = int(input("Guess the number"))
        chances -= 1
    elif guess > number  :
        print("Your guess is too high, guess a number lower than", guess)
        guess = int(input("Guess the number"))
        chances -= 1


