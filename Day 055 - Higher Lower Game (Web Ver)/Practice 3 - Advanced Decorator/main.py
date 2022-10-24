# Create the logging_decorator() function 👇

def logging_decorator(function: object) -> object:
  def wrapper(*args):
    returned = function(*args)
    print(f"You called: {function.__name__}")
    print(f"Using the following Arguments: {args}")
    print(f"It returned: {returned}")

  return wrapper



# Use the decorator 👇

@logging_decorator
def adder(a,b):
  return a+b

@logging_decorator
def concat(string1, string2, string3):
  return f"{string1} {string2} {string3}"



adder(2,5)

concat("Hello", "There", "General Kenobi")