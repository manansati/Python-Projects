import random
import os

print("Brute Force Attack by Manan Sati")
password = input("Enter a Password: ")
os.system("clear")

words = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
guess = ""

while guess != password:
    guess = ""
    for _ in range(len(password)):
        guess += random.choice(words)
    
    print(f"Trying: {guess}")

print(f"\nYour Password is: {guess}")
