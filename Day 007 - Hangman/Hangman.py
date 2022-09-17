import random
import hangman_art
import hangman_words

#word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
display = ""
for i in chosen_word:
    display += "_"

new_display = ""
end_game = False
lives = 6
guessed_letters = ""

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

print(hangman_art.logo)
print("\n")

while not end_game:
    print(display+"\n")
    guess = input("Guess a letter in the word...   ").lower()

    if(guess not in guessed_letters):
        for i in range(len(chosen_word)):
            if chosen_word[i]== guess:
                new_display += guess
            else:
                new_display += display[i]

        if(display == new_display):
            lives -= 1
        else:
            display = new_display

        new_display = ""
    else:
        print("You already guessed '"+guess+"'.")
    
    guessed_letters += guess


    if(chosen_word == display):
        end_game = True
        print("You Win!")

    if lives <= 0:
        end_game = True
        print("You lose, the word was: " + chosen_word)
    
    print(hangman_art.stages[lives])
