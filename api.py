# // create command line game rock paper scissors with python and fastAPI
# // and the game should be game loop and count gampe played and print game winds
# // add Lizard and Spock to the game

from fastapi import FastAPI
import random

app = FastAPI()

wins = 0
losses = 0
played = 0

choices = ['rock','paper','scissor','lizard','spock']

# // create post api played will push playerCoice as body and the api will return
# // the result of the game like computerChoice, Winer, winds, looses, gamePlayed

@app.post("/play")
async def play(playerChoice: str):
    global wins
    global losses
    global played

    if playerChoice not in choices:
        return "Please input valid choice"

    computer = random.choice(choices)
    print(f"The computer choice : {computer}")
    print(f"The player choice : {playerChoice}")

    if playerChoice == computer:
        played += 1
        return {"computerChoice": computer, "result": 'It\'s a tie', "wins": wins, "losses": losses, "played": played}

    # r > s, s > p, p > r
    if is_win(playerChoice, computer):
        played += 1
        wins += 1
        return {"computerChoice": computer, "result": 'P', "wins": wins, "losses": losses, "played": played}
    losses += 1
    played += 1
    return {"computerChoice": computer, "result": 'C', "wins": wins, "losses": losses, "played": played}

def is_win(player, opponent):
    def is_win(player, opponent):
    
    # // add Lizard and Spock to the game
    if (player == 'rock' and opponent == 'lizard') or (player == 'lizard' and opponent == 'spock') \
        or (player == 'spock' and opponent == 'scissor') or (player == 'scissor' and opponent == 'lizard') \
        or (player == 'lizard' and opponent == 'paper') or (player == 'paper' and opponent == 'spock') \
        or (player == 'spock' and opponent == 'rock') or (player == 'rock' and opponent == 'scissor') \
        or (player == 'scissor' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True

        




