from tkinter import *

def clicked():
    new_text = input.get()
    my_label.config(text= new_text)

window = Tk()
window.title("this is the title")
window.minsize(height= 300, width= 500)
window.config(padx= 20, pady= 20)


#label
my_label = Label(text="this is a label")
my_label["text"] = "New Text"
my_label.config(text="New Text", pady=50, padx= 50)
my_label.grid(column = 0, row = 0)

#button

button = Button(text="this is a button", command=clicked)
button2 = Button(text="new button")
button.grid(column = 1, row = 1)
button2.grid(column = 2, row = 0)
#entry

input = Entry(width= 20)
input.grid(column = 3, row = 2)



window.mainloop()



