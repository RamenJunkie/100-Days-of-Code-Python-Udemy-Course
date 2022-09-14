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
