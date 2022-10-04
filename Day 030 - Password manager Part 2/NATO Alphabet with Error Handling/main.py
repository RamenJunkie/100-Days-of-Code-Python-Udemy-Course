import pandas
FILE = "nato_phonetic_alphabet.csv"

data = pandas.read_csv(FILE)
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#print(nato_dict)

def convert():
    try:
        translate_word = input("Please enter the word to translate: ").upper()
        nato_word = [nato_dict[letter] for letter in translate_word]
    except KeyError:
        print("Only Letter Accepted")
        return convert()

    return nato_word

nato_word = convert()
print(nato_word)

