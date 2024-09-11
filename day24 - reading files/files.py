# file = open("my_file") #store this to access files
#
# contents = file.read() #allows you to see what is written in files
#
# print(contents)
# file.close() #closes this file manually

with open("my_file") as file: #closes automatically, automatically done in read only mode.
    contents = file.read()
    print(contents)

with open("my_new_file", mode="w") as file: #writes over existing files mode = "w" mean write, makes new file auto
    file.write("new text")


with open("my_file", mode= "a") as file:
    file.write("\nbut my name is Ruby")
