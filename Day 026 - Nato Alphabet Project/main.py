import pandas
FILE = "nato_phonetic_alphabet.csv"

data = pandas.read_csv(FILE)
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#print(nato_dict)

translate_word = input("Please enter the word to translate: ").upper()
nato_word = [nato_dict[letter] for letter in translate_word]

print(nato_word)

