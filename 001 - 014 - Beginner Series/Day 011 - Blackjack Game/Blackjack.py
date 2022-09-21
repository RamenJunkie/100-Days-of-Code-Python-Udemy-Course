############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.
# Use zero hints.....

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from Blackjack_art import logo

K = 10
Q = 10
J = 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
valid_actions = ["h", "s", "hit", "stand"]
continue_on = True
selection = ""

print(logo)


def deal_card(hand):
    hand.append(random.choice(cards))
    return hand


def total_cards(hand):
    if sum(hand) > 21 and (11 in hand):
        hand[hand.index(11)] = 1
    return sum(hand)


while (continue_on):
    player_cards = []
    dealer_cards = []
    action = "hit"
    win_loss = ""
    dealer_round = True
    player_cards = deal_card(player_cards)
    dealer_cards = deal_card(dealer_cards)
    player_cards = deal_card(player_cards)
    dealer_cards = deal_card(dealer_cards)

    #Player round
    while (action == "hit" or action == "h"):
        print(
            f"Your current hand: {player_cards}, total {total_cards(player_cards)}"
        )
        print(f"Dealer is showing: [{dealer_cards[0]}, X]")
        action = ""
        while (action not in valid_actions):
            action = input("Would you like to (H)it or (S)tand? ").lower()

        if action == "hit" or action == "h":
            player_cards = deal_card(player_cards)

        if total_cards(player_cards) > 21:
            action = "stand"
            dealer_round = False
            win_loss = "loss"

    #Dealer round
    print(
        f"Player has finished with {player_cards}, Dealer has {dealer_cards}, total {total_cards(dealer_cards)}."
    )

    while (dealer_round):
        if(total_cards(dealer_cards) == 21 and len(dealer_cards) == 2):
            print("Dealer has Blackjack.")
            dealer_round = False
        elif total_cards(dealer_cards) >= 17:
            dealer_round = False
        else:
            dealer_cards = deal_card(dealer_cards)

        print(f"Dealer has {dealer_cards}, total {total_cards(dealer_cards)}.")

    if total_cards(dealer_cards) > 21:
        win_loss = "bust"
        dealer_round = False
    elif total_cards(dealer_cards) > total_cards(player_cards):
        win_loss = "dealer"
        dealer_round = False
    elif total_cards(dealer_cards) == total_cards(player_cards):
        win_loss = "push"
        dealer_round = False

    if win_loss == "loss":
        print(f"Player has busted with {player_cards}, {total_cards(player_cards)} total  and loses the round.")
    elif win_loss == "bust":
        print(f"Dealer has busted with {dealer_cards}, {total_cards(dealer_cards)} the player wins!")
    elif win_loss == "dealer":
        print(
            f"Dealer has won the round with a total of {total_cards(dealer_cards)}."
        )
    elif win_loss == "push":
        print(f"It's a push with a score of {total_cards(player_cards)}")
    else:
        print(
            f"Player has won with a total of f{total_cards(player_cards)}.  Congratulations!"
        )

    selection = input("You you like to play another round? Y/N ").lower()

    if selection == "n" or selection == "no":
        print("Thank you for playing!")
        continue_on = False
