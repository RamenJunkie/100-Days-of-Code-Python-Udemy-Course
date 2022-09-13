# Exercise 1 - Odd or Even

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if(number % 2 == 0):
    print("This is an even number.")
else:
    print("This is an odd number.")



#Exercise 2 - BMI v 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(float(weight) / (float(height)**2))

if(BMI < 18.5):
    BMI_desc = "are underweight"
elif(BMI <= 25):
    BMI_desc = "have a normal weight"
elif(BMI <= 30):
    BMI_desc = "are slightly overweight"
elif(BMI <= 35):
    BMI_desc = "are obese"
else:
    #OH LORD HE COMMIN!
    BMI_desc = "are clinically obese"


print(f"Your BMI is {BMI}, you {BMI_desc}.")



# Exercise 3 - Leap Years

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

is_leap = "Not leap year."

if(year % 4 == 0):
    is_leap = "Leap year."

if(year % 100 == 0 and year % 400 !=0):
    is_leap = "Not leap year."

print(is_leap)




# Exercise 4 - Pizza Prices

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total = 0

if(extra_cheese == 'Y'):
    total +=1

if(size == "S"):
    total+=15
elif(size == "M"):
    total+=20
else:
    total+=25

if(add_pepperoni == "Y"):
    total+=3
    if(size == "S"):
        total -= 1


print(f"Your final bill is: ${total}.")





#Exercise 5 - Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true_count = 0
love_count = 0

for i in "true":
    true_count += name1.lower().count(i) + name2.lower().count(i)
for i in "love":
    love_count += name1.lower().count(i) + name2.lower().count(i)

truelove = int(str(true_count) + str(love_count))

if(truelove < 10 or truelove > 90):
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif(40 < truelove < 50):
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}.")