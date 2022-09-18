from replit import clear
import silent_auction_art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

auctions = {}
new_bidder = True
highest = 0
winner = ""

def new_bid():
  name = input("What is the name of the bidder? ")
  bid = input(f"What is {name}'s bid? ")
  auctions[name] = int(bid)

def more_bidders():
  go_on = input("Are there any more bidders? ").lower()

  if(go_on == "yes" or go_on == "y"):
    return True
  else:
    return False

while(new_bidder):
  new_bid()
  new_bidder = more_bidders()
  clear()

for person in auctions:
  if(auctions[person] > highest):
    highest = auctions[person]
    winner = person

print(f"The auction is over, the winner is..... {winner} for ${highest}!")