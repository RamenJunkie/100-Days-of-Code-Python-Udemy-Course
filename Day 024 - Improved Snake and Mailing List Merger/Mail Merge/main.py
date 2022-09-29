names_file = "Input/Names/invited_names.txt"
letter_file = "Input/Letters/starting_letter.txt"

names = open(names_file, "r")
#debug print(names.readlines())
name_list = names.readlines()
letter_text = open(letter_file, "r")
#debug print(letter_text.readlines())
letter_lines = letter_text.readlines()
names.close()
letter_text.close()

for name in name_list:
    cur_name = name.strip("\n")
    new_letter = []
    #debug print(cur_name)
    for line in letter_lines:
        new_letter.append(line.replace("[name]",cur_name))

    #debug print(new_letter)
    fileout = "Output/ReadyToSend/Letter_to_"+cur_name+".txt"
    writer = open(fileout, "w")
    for nextline in new_letter:
        writer.writelines([nextline])
    writer.close()