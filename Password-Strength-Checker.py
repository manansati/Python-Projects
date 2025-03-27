# Password Strength Checker By Manan Sati
import os
import sys


print("Password Strength Checker By Manan Sati")
password=input("Enter Your Password: ")
for i in range (len(password)):
    if password[i].islower == True:
        continue
    elif password[i].isupper == True:
       continue
    elif password[i].isdigit == True:
        continue
    else:
        print("Weak Password")
x=input("")