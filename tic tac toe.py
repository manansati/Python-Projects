import time 
import random
print("Tic Tac Toe by Manan")
name=input('enter you name: ').title()
start = time.time()

r1 = [' ', ' ', ' ']
r2 = [' ', ' ', ' ']
r3 = [' ', ' ', ' ']

def board():
    print()
    print(r1[0], '|', r1[1], '|', r1[2])
    print('--+---+--')
    print(r2[0], '|', r2[1], '|', r2[2])
    print('--+---+--')
    print(r3[0], '|', r3[1], '|', r3[2])
    print()

def place(move, symbol):
    if move == 1:
        r1[0] = symbol
    elif move == 2:
        r1[1] = symbol
    elif move == 3:
        r1[2] = symbol
    elif move == 4:
        r2[0] = symbol
    elif move == 5:
        r2[1] = symbol
    elif move == 6:
        r2[2] = symbol
    elif move == 7:
        r3[0] = symbol
    elif move == 8:
        r3[1] = symbol
    elif move == 9:
        r3[2] = symbol

def check():
    if r1[0] == r1[1] == r1[2] != ' ':
        return r1[0]
    if r2[0] == r2[1] == r2[2] != ' ':
        return r2[0]
    if r3[0] == r3[1] == r3[2] != ' ':
        return r3[0]
    if r1[0] == r2[0] == r3[0] != ' ':
        return r1[0]
    if r1[1] == r2[1] == r3[1] != ' ':
        return r1[1]
    if r1[2] == r2[2] == r3[2] != ' ':
        return r1[2]
    if r1[0] == r2[1] == r3[2] != ' ':
        return r1[0]
    if r1[2] == r2[1] == r3[0] != ' ':
        return r1[2]
    return None

def empty(m):
    if m == 1: 
        return r1[0] == ' '
    if m == 2: 
        return r1[1] == ' '
    if m == 3: 
        return r1[2] == ' '
    if m == 4: 
        return r2[0] == ' '
    if m == 5: 
        return r2[1] == ' '
    if m == 6: 
        return r2[2] == ' '
    if m == 7: 
        return r3[0] == ' '
    if m == 8: 
        return r3[1] == ' '
    if m == 9: 
        return r3[2] == ' '

def easy():
    possible_moves = []
    for pos in range(1, 10):
        if empty(pos):
            possible_moves.append(pos)
    return random.choice(possible_moves)



def player_play(turn="X"):
    while True:
        try:
            m = int(input(f"{turn}'s turn — Enter position (1-9): "))
            if m < 1 or m > 9:
                print("Invalid! Choose 1–9.")
            elif not empty(m):
                print("Spot taken!")
            else:
                return m
        except:
            print("Enter a number only!")

turn = "X"
board()
f=open('score.txt','a+')

for i in range(9):
    if turn == "X":
        m = player_play("X")
        place(m, "X")
    else:
        m = easy()
        place(m, "O")
        time.sleep(1)

    board()

    winner = check()
    if winner:
        print(winner, "wins!")
        end = time.time()
        samay=(end-start)
        now = time.localtime()
        t=(f"{name} : {samay:.1f}s - {time.strftime('%Y-%m-%d %H:%M:%S', now)}\n")
        print(t)
        f.write(t)
        f.seek(0)
        text=f.read()
        hs=input("Do you want to know all scores? ").lower()
        if hs in ("1", "yes", "y"):
            print(text)
        f.close()
        break

    turn = "O" if turn == "X" else "X"

else:
    print("It's a draw!")
