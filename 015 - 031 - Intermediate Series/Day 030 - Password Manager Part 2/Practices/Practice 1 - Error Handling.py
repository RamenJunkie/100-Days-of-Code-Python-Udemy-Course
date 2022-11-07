#FileNotFound
#with open("non-existent.txt") as file:
#    file.read()

#try:
#    file = open("file.txt")
#    a_dictionary = {"key":"value"}
#    print(a_dictionary["key"])
#except FileNotFoundError:
#    #print("There was an error")
#    file = open("file.txt", "w")
#    file.write("Something")
#except KeyError as error_message:
#    print(f"Key Error: {error_message}")
#else:
#    content = file.read()
#    print("It worked!")
#finally:
#    file.close()
#    print("File Was Closed")
#    raise KeyError("REREEEEEEE")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height is too high, sorry Godzilla.")

bmi = weight / height **2

print(bmi)






