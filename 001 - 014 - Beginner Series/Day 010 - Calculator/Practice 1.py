#Functions with Outputs

def format_name(f_name, l_name):
    f_name = f_name.title() 
    l_name = l_name.title()
    return (f_name + " " + l_name)

first = input("What is the first name? ")
last = input("What is the last name? ")

full_name = format_name(first,last)

print(f"The corrected name is {full_name}.")