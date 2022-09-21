# An alternate version of get_money from main.py
# This version asks for coins one at a time until paid.

def get_money(drink):
    global total_money
    total_coins = 0
    coin = ""
    price = MENU[drink]["cost"]
    while(total_coins < price):
        print(f"A {drink} is ${round(price, 2)}, please pay an additional {round((price - total_coins),2)}.")
        while coin not in valid_coins:
            coin = input("Please insert a coin... (Q)uarter, (D)ime, (N)ickle), (C)ancel Transaction ").lower()

        if(coin[0:] == "c"):
            return False
            print("Transaction Cancelled")
        else:
            total_coins += COINS[coin]
        coin = ""
    if(total_coins > price):
        print(f"Here is your change: ${round((total_coins - price), 2)}")

    total_money += price
    return True