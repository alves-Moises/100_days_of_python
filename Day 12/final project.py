#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint as rint
from replit import clear

def check_value(player, ai):
    if player > ai:
        print("Too high")
    else:
        print("Too low")

def main():
    numb = rint(1, 100)

    dificulty = {"1": 10, "2":5}
    lifes = dificulty[input("Delect your dificult: \n[1] Easy \n[2] Hard")]
    
    win = False
    while lifes > 0 and not win:
        choice = int(input("A number: "))
        if choice == numb:
            win = True
            print("You win!")
            break

        clear()
        check_value(choice, numb)
        lifes -= 1
        print(f"lifes: {lifes}")
main()

