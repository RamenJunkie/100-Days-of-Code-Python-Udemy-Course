Dictionary Notes:

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Bug"])

# Add an entry
# Edit an entry
programming_dictionary["Code"] = "A set of instructions used to make the computer do something."

print(programming_dictionary["Code"])

print(programming_dictionary)

# Also Whipes a dictionary
empty_dictionary = {}

# Loop through a dictonary
Get all keys: 

for thing in dictionary:
    print(thing)
# Print Value
    print(dictionary[thing])



----------------------------------------------------------

##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]