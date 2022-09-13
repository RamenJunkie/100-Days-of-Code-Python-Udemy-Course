# Exercise 1 - Data Types

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first = int(two_digit_number[0])
second = int(two_digit_number[1])

print (first+second)

#Exercise 2 - BMI

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = float(weight) / (float(height)**2)

print(round(BMI))

#Exercise 3 - Life in Weeks

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

left = 90-int(age)
# Crappy
print("You have " + str(left*365) + " days, " + str(left*52) + " weeks, and " + str(left*12) + " months left.")
#f-string
print(f"You have {left*365} days, {left*52}  weeks, and {left*12} months left.")

