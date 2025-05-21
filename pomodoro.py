import os
import sys
import pygame
import time

# A Pomodora Productive App by Manan

def counter(xx):
    os.system('clear')
    for i in range (xx,0,-1):
        mins=i//60
        secs=i%60
        if secs < 10:
            print(f'Timer: {mins}:0{secs}')
        else:
            print(f'Timer: {mins}:{secs}')
        time.sleep(1)
        os.system('clear')

def alarm(xxx):
    print('Beep Beep')
    for i in range (xxx):
        print('\a',end='',flush=True)
        time.sleep(0.3)
        os.system('clear')



while True:
    print('A productive pomodoro app by Manan')
    x=int(input('Please select mode:\n1-Default Timers\n2-Custom Timer\n3-Stopwatch\n4-Exit\n\n'))
    os.system('clear')

    if x == 4:
        sys.exit()
    elif x == 2:
        timee = int(input("Enter Custom Duration in mins: "))
        time_sec=timee*60
        counter(time_sec)
        alarm(30)
    elif x == 1:
        z=int(input('1-25:5\n2-50:10\n3-Back\n\n'))
        os.system('clear')
        if z == 1:
            counter(1500)
            alarm(30)
            counter(300)
            alarm(30)
        elif z == 2:
            counter(3000)
            alarm(30)
            counter(600)
            alarm(30)
        else:
            None
    


