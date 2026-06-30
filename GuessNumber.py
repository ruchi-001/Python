import random

print("Hi! Welcome to the Number Guessing Game. Let's start")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 5 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high) 
# Total allowed chances
chances = 5
# Guess counter
guessCount = 0                         

while guessCount < chances:
    guessCount += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'you guessed it correctly!')
        break

    elif guessCount >= chances and guess != num:
        print(f'Game Over! The correct number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')
