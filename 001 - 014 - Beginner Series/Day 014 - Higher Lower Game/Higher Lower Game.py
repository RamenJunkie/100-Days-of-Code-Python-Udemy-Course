import hl_art
from hl_data import data
import random


def pic_account():
    return data[random.randint(1, len(data))]


def compare_follows(a, b):
    if a > b:
        return True
    else:
        return False


account_a = pic_account()
choice = ""
valid_choices = ['a', 'b']
score = 0
winner = True

print(hl_art.logo)

while (winner):
    account_b = pic_account()
    # Make sure they aren't the same account
    while (account_b['name'] == account_a['name']):
        account_b = pic_account()

    #name, follower_count, description, country
    print(
        f"A: {account_a['name']}, a {account_a['description']} from {account_a['country']}"
    )
    #debug print(account_a['follower_count'])
    print(hl_art.vs)
    print(
        f"B: {account_b['name']}, a {account_b['description']} from {account_b['country']}"
    )
    #debug print(account_b['follower_count'])

    while choice not in valid_choices:
        choice = input(
            "Who has the higher follower count, (A or B)?\n").lower()

    if (choice == "a"):
        winner = compare_follows(account_a['follower_count'],
                                 account_b['follower_count'])
    else:
        winner = compare_follows(account_b['follower_count'],
                                 account_a['follower_count'])

    choice = ""
    #debug print(winner)

    if (winner):
        score += 1
        account_a = account_b
        print(
            f"\n\nThat's correct!  Your score is {score}.\n\n **********************************************\n\n"
        )

print(f"\n\nSorry, that's incorrect, your final score was {score}.")
