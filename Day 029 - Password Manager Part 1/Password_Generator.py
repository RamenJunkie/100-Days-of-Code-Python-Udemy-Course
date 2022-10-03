#Password Generator Project
import random

class pass_gen():

    def __init__(self):
        pass

    def make_password(self):
        letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(4,8)
        nr_symbols = random.randint(3,4)
        nr_numbers = random.randint(3,4)

        password = [random.choice(letters) for n in range(nr_letters)]
        password += [random.choice(numbers) for n in range(nr_numbers)]
        password += [random.choice(symbols) for n in range(nr_symbols)]

        random.shuffle(password)

        return "".join(password)



