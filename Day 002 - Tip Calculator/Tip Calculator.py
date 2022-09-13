#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Tip Calculator")
total_bill = float(input("What was the bill total?\n"))
percentage = int(input("What percentage of tip would you like to give?\n (Suggested: 10%, 12%, 15%\n"))
total_peeps = int(input("How many people are paying?\n"))

total_with_tip = total_bill*(1+1/percentage)
each_pay = round(total_with_tip/total_peeps, 2)

print(f"Each person will pay: ${each_pay}")