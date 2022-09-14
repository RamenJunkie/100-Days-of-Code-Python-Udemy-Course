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
