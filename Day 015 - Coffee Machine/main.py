from menu import MENU
from logo import logo

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 100,
}

total_money = 0

def print_report():
    for i in resources:
        print(f"Remaining {i}: {resources[i]}")
    print("Total Sales: ${:.2f}".format(total_money))

def make_drink(drink):
    for ing in MENU[drink]["ingredients"]:
            resources[ing] = resources[ing] - MENU[drink]["ingredients"][ing]
    

def check_levels(drink):
    for ing in MENU[drink]["ingredients"]:
        if( MENU[drink]["ingredients"][ing] > resources[ing] ):
            return False
    return True

def get_money(drink):
    global total_money
    total_coins = 0
    price = MENU[drink]["cost"]
    print ("A {} is ${:.2f}".format(drink,price) )
    quart = int(input("How many Quarters? "))
    dime = int(input("How many Dimes? "))
    nickle = int(input("How many Nickles? "))

    total_coins = quart * .25 + dime * .10 + nickle * .05

    if(total_coins > price):
        print("Here is your change: ${:.2f}".format(total_coins - price))
    elif(total_coins < price):
        print("Not enough money, please order again.")
        return False

    total_money += price
    return True

user_menu = []
for i in MENU:
    user_menu.append(i)

valid_choices = []
valid_choices += user_menu
valid_choices.append("report")
valid_choices.append("off")
choice = ""
online = True

while(online):
    print(logo)
    while choice not in valid_choices:
        choice = input(f"What would you like to order? {user_menu} ").lower()

    if(choice == "report"):
        print("Pritning report...")
        print_report()
    elif(choice == "off"):
        print("Going offline for repair...")
        print("Final report...")
        print_report()
        online = False
    else:
        good_levels = check_levels(choice)

        if(good_levels):
            good_money = get_money(choice)
        else:
            print("Sorry, that item is sold out.")

        if(good_money and good_levels):
            make_drink(choice)
            print(f"Thank you, enjoy your {choice}.")
    choice = ""


