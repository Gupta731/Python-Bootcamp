with open("./Input/Letters/starting_letter.txt") as file:
    start_letter = file.read()
    # print(start_letter)

with open("./Input/Names/invited_names.txt") as invited:
    names = invited.read()
    name_list = names.split('\n')
    # print(name_list)

for name in name_list:
    new_file = open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")
    new_letter = start_letter.replace('[name]', name)
    new_file.write(new_letter)
    new_file.close()
