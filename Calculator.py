# CLI based Calculator by Manan Sati
import os 
def clear():
    os.system('clear') if os.name=='posix' else os.system('cls')

clear()
print("CLI Calculator by Manan")
temp=input("Press enter to Continue ")

while True:
    try:
        operation=int(input("1-Add\n2-Substract\n3-Multiply\n4-Devide\n5-exit\n\n"))

        if operation ==5:
            clear()
            break
        clear()

        num1=float(input("Enter a Number: "))
        num2=float(input('Enter another Number: '))

        if operation == 1:
            print(num1+num2)
        elif operation == 2:
            print(num1-num2)
        elif operation == 3:
            print(num1*num2)
        elif operation ==4:
            print(num1/num2)
        else:
            print("Invalid Input, Try again")
        temp=input("Press enter to Continue ")
        clear()
    except:
        clear()
        print("Error!!")
        temp=input("Press enter to Continue ")
        clear()
