rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

computer_choice = random.randint(0,2)

rps = [rock, paper, scissors]

win_conditions = [["Draw","Opponent","Player"],["Player","Draw","Opponent"],["Opponent","Player","Draw"]]

print("Welcome to Rock Paper Scissors \n")
check = True
while(check):
  choice = input("Please make your choice 0 - Rock, 1 - Paper, or 2 - Scissors\n")

  if(choice == "0" or choice == "1" or choice == "2"):
    choice = int(choice)
    check = False
  else:
    print("Invalid choice.\n")

print("Player chooses: \n" + rps[choice])

print("Opponent chooses: \n" + rps[computer_choice])

print("The winner is: " + win_conditions[choice][computer_choice])
