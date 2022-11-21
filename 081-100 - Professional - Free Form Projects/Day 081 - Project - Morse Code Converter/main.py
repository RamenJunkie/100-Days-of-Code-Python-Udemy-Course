import winsound
from time import sleep

# Morse Code
morse_code = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}

# Loop Variable
keep_going = True
valid_answers = ["yes","y","no","n"]

# Sound Variables
frequency = 700  # Set Frequency To 2500 Hertz
duration_short = 100  # Set Duration To 100 ms == .1 second
duration_long = 300  # Set Duration To 300 ms == .3 second

while keep_going:
    # Get String of Text to Convert
    conversion_string = input("Please enter a string to convert to Morse Code:\n").lower()
    # Fresh Code String Each Time
    code_string = ""
    # Do the Conversion
    for letter in conversion_string:
        if letter in morse_code:
            code_string += morse_code[letter]+" "
        else:
            code_string += letter
    # Show the Result
    print("Your Morse Code is:\n")
    print(code_string)
    # Ask if the user wants to hear the sound
    go_on = ""
    while go_on not in valid_answers:
        go_on = input("Would you like to play this sound? (Yes/No) ").lower()
    # If Yes, Play the sound
    if go_on == "yes" or go_on == "y":
        for beep in code_string:
            #print(beep)
            if beep == "−":
                winsound.Beep(frequency, duration_long)
            elif beep == "·":
                winsound.Beep(frequency, duration_short)
            # Needs a brief pause
            sleep(.05)

    # See if the user wants to do another conversion.
    go_on = ""
    while go_on not in valid_answers:
        go_on = input("Translate another string? (Yes/No) ").lower()
    # Quit if no more conversions
    if go_on == "no" or go_on == "n":
        keep_going = False