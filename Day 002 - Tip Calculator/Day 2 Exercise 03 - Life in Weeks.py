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