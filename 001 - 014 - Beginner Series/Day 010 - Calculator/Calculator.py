# Calculator App for 100 Days of Code - Pythin App Brewey Course

import Calculator_art


def add(n1, n2):
    """Add two numbers"""
    return n1 + n2


def sub(n1, n2):
    """Subtract two numbers"""
    return n1 - n2


def mult(n1, n2):
    """Multiply 2 numbers"""
    return n1 * n2


def div(n1, n2):
    """Divide two numbers"""
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}


def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list




def calculator():
    print(Calculator_art.logo)
    continue_on = True
    operation = ""
    valid_replies = ["yes", "y", "no", "n", "quit", "q"]

    num1 = float(input("Please enter the first number: "))

    while (continue_on):
        followup = ""
        operation = ""

        while (operation not in getList(operations)):
            operation = input(
                f"Which operation would you like to perform? {getList(operations)} "
            )
        num2 = float(input("Please enter the next number: "))
        function = operations[operation]
        result = function(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        while followup not in valid_replies:
            followup = input(
                "Would you like to perform another opertion on the result (Y), a new operation(N) or Quit (Q)? "
            ).lower()

        if (followup == "no" or followup == "n"):
            continue_on = False
            calculator()
        elif (followup == "quit" or followup == "q"):
            return
        else:
            continue_on = True

        num1 = result

calculator()