#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_chars = nr_letters+nr_symbols+nr_numbers
password = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for i in range(1, nr_letters + 1):
    #password += random.choice(letters)
    password = password + (letters[random.randint(0, 25)])
for i in range(1, nr_symbols + 1):
    password = password + (symbols[random.randint(0, 8)])
for i in range(1, nr_numbers + 1):
    password = password + (numbers[random.randint(0, 9)])

print(password)

password =""

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

while((nr_letters+nr_numbers+nr_symbols) > 0):
  type = random.randint(1,3)
  if(type == 1 and nr_letters >0):
    password = password + (letters[random.randint(0, 25)])
    nr_letters -= 1
  if(type == 2 and nr_symbols >0):
    password = password + (symbols[random.randint(0, 8)])
    nr_symbols -= 1
  if(type == 3 and nr_numbers >0):
    password = password + (numbers[random.randint(0, 9)])
    nr_numbers -= 1

print(password)
