#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from Guesser_art import logo

lives = 0
win = False
unknown = random.randint(1, 100)
difficulties = {
    "easy": 10,
    "e": 10,
    "hard": 5,
    "h": 5,
    "cheat": 10000,
}


def check_guess(guess):
    if guess > 100 or guess < 0:
        print(
            "You seem to be having some difficulty understanding the concept here..."
        )
    elif (guess > unknown):
        print("Too high.")
    elif (guess < unknown):
        print("Too low")
    else:
        print("You got it!")
        return True
    return False


print(logo)

print("Welcome to Gue??, the number guessing game.\n")
print("Guess a number between 1 and 100.")
lives = difficulties[input("Choose a difficulty, Easy or Hard: ").lower()]

while not win:
    print(f"You have {lives} attempts to guess the number.")
    win = check_guess(int(input("Make a guess: ")))
    lives -= 1