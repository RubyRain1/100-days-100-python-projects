#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("./Input/Names/invited_names.txt") as file2:
    names = file2.readlines()


with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()
    content.strip()
    for i in names:
        i = i.strip()
        with open(f"letter_for_{i}.txt", mode="w") as note:
            x = content.replace("[name]", i)
            note.write(x)
