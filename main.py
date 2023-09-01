

# Path: main.py
# // create command line game rock paper scissors with python
# // and the game should be game loop and count gampe played and print game winds

import random

wins = 0
losses = 0
played = 0

choices = ['rock','paper','scissor'] 

def play():
    user = input("Please input your choice: ")
    if user not in choices:
        print("Please input valid choice")
        return
    computer = random.choice(choices)
    print(f"The computer choice : {computer}")
    print(f"The player choice : {user}")

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'P'
    return 'C'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'rock' and opponent == 'scissor') or (player == 'scissor' and opponent == 'paper') \
        or (player == 'paper' and opponent == 'rock'):
        return True

while True:
    result = play()
    if result == 'P':
        print('The winer is player')
        wins += 1
    elif result == 'C':
        print('The winer is computer')
        losses += 1
    
    played += 1
    print(f"Played: {played}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print("==================")

    if played == 99:
        break



