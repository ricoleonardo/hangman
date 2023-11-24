from os import system
from playsound import playsound

def new_board():
    board = ("\u0332".join("| 1 | 2 | 3 |\n") + "\u0332".join("| 4 | 5 | 6 |\n") + ("| 7 | 8 | 9 |\n")) # list
    print(board)

def new_board(spot): # \n is new line
    board = (f" | {spot[1]} | {spot[2]} | {spot[3]} |\n"
             f" | {spot[4]} | {spot[5]} | {spot[6]} |\n"
             f" | {spot[7]} | {spot[8]} | {spot[9]} |\n")
    print(board)

def who_wins(spot):
    # Horizontal (\ is the end is line continuation)
    if     (spot[1] == spot[2] == spot[3]) \
        or (spot[4] == spot[5] == spot[6]) \
        or (spot[7] == spot[8] == spot[9]):
        return True
    # Vertical
    elif   (spot[1] == spot[4] == spot[7]) \
        or (spot[2] == spot[5] == spot[8]) \
        or (spot[3] == spot[6] == spot[9]):
        return True
    # Diagonal 
    elif     (spot[1] == spot[5] == spot[9]) \
        or   (spot[3] == spot[5] == spot[7]):
        return True
    else: return False


def whose_turn(turn):
    if turn % 2 == 0: return "\xd8" # ascii code
    else: return "X"

spot = {1 : "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"} # dictionary

turn = 0
end = False
play = True
p_turn = -1

while play:
    # to clear the screen
    system('cls')
    new_board(spot) # load the board
    #if invalid turn occured
    if p_turn == turn:
        print("Invalid Detected, please pick another one")
    p_turn = turn

    print("Player " + str((turn%2)+1) + " 's turn: Pick Spot or press q to quit")

    #get input

    typeanumber = input()
    playsound('MiniGame\swoosh.mp3')

    if typeanumber == "q":
        play = False
    elif str.isdigit(typeanumber) and int(typeanumber) in spot: # error handling to input only digits
        if not spot[int(typeanumber)] in {"X", "0"}:
            turn += 1
            spot[int(typeanumber)] = whose_turn(turn)

    #who wins
    if who_wins(spot): play, end = False, True
    if turn > 8: play = False

system('cls') # clear the screen
new_board(spot) # load the board

if end:
    if whose_turn(turn) == 'X': 
        print("\033[1;31;40m Player 1 Wins! \033[0m")
        playsound('MiniGame\yahoo.mp3')

    else: 
        print("\033[1;32m Player 2 Wins! :) \033[0m")
        playsound('MiniGame\yahoo.mp3')

else:
    #No WInner
    playsound('MiniGame\mancry.mp3')
    print("No Winner :(")



