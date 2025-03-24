# Password Generator by Manan
import random
import os

try:
    length=int(input("Enter the length of the Password: "))
except:
    print("Please enter a valid number and try again ")
    os.system('exit')

words=('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()')

password=''
for i in range (length):
    temp=random.randint(0,len(words))
    password+=words[temp]


print(f"Your Password is: {password}")