from tkinter import *


window = Tk()

window.title("this is the title")
window.minsize(height= 500, width= 300)



#label
my_label = Label(text="this is a label")
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
#button

def clicked():
    new_text = input.get()
    my_label.config(text= new_text)



button = Button(text="this is a button", command=clicked)
button.pack()

#entry

input = Entry(width= 20)
input.pack()



window.mainloop()



