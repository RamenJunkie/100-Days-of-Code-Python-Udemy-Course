If you run the program in a DOS/Linux terminal you could use this (or the following one too):

    import os
     
    def clear():  # Cross-platform clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

The above will not work in the PyCharm output (Run) console. Use this instead:

    def clear():  # Prints 50 blank lines
        print("\n" * 50)