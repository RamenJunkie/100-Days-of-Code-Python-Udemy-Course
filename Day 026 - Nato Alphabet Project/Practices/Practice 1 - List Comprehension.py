
# add one to each number in a list
numbers = [1,2,3,4,5]
new_list = []
for i in numbers:
    add_one = i+1
    new_list.append(add_one)

print(new_list)

# using list comprehension

new_list2 = [item+1 for item in numbers]

print(new_list2)

name = "Angela"
new_list3 = [letter for letter in name]
print(new_list3)

new_list4 = [n*2 for n in range(1,5)]
print(new_list4)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
new_list5 = [nextname.upper() for nextname in names if len(nextname) > 5]
print(new_list5)