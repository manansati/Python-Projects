# A simple unit conveter by Manan Sati
import sys
import os
def clr():
    os.system('clear')
while True:
    print("A simple unit conveter by Manan")
    try:
        inp=int(input("1-Km to Miles\n2-C to K\n3-Kg to lb\n4-Exit\n"))
    except:
        print("Invalid option, please try again")
        sys.exit()
    clr()
    if inp==1:
        km=float(input("Km="))
        mile=km*0.621371
        print(f"{km}kms = {mile:.2f}miles")
    elif inp==2:
        c=float(input("C="))
        f=(c*9/5) + 32
        print(f"{c}C = {f:.2f}F")
    elif inp==3:
        kg=float(input("kg="))
        lb=kg*2.20462
        print(f"{kg}Kgs = {lb:.2f}Lbs")
    elif inp==4:
        sys.exit()
    else:
        print("invalid output, please try again!")
    x=input("Press Enter to Continue")
    clr()
