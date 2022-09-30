### Square Numbers in a List
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number * number for number in numbers]

#Write your code 👆 above:

print(squared_numbers)



### Even Numbers Only
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]


#Write your code 👆 above:

print(result)



## Compare 2 lists

with open("list1.txt") as data:
    list1 = data.readlines()
with open("list2.txt") as data:
    list2 = data.readlines()

print(list1)
print(list2)

result = [int(num) for num in list1 if (num in list2)]

# Write your code above 👆

print(result)


