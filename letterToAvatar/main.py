with open("./Names/invited_names.txt", "r") as names:
    name = names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letters = letter.read()
    for n in name:
        new_letter = (letters.replace("[name]", n))

with open("./Output/ReadyToSend", "w") as letterTo:
    pass
