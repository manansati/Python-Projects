# Number Guessing Game by Manan
import random
import sys

print("Number Guessing Game by Manan")

num= random.randint(1,100)
attempts=0
while attempts < 10:
    attempts+=1
    try:
        guess=int(input("Guess a Number Between 1-100: "))
    except:
        print("Please enter a valid number and try again!")
        sys.exit()
    if guess == num:
        print(f'Congratulations, you guessed the number in {attempts} attempts!')
        break
    elif guess < num:
        print('Too low! Try Again')
    else:
        print('Too High! Try Again')

print(f"The correct number was {num}") if guess!=num else None