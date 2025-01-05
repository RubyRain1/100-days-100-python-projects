from tkinter import *


def convertclick():
    miles = int(convertor_input.get())
    km = miles * 1.609344
    result_label.config(text= km)

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=250, height=150)
window.config(pady=40)
# column 0: 1 label
#column 1: 1 entry, 1 label, 1 button
#column 2: 2 labels

#labels
filler_label = Label(text="")
equal_label = Label(text= "Is equal to")
result_label = Label(text = "0")
miles_label = Label(text= "Miles")
kilomet_label = Label(text= "KM")

filler_label.grid(column = 0, row = 0)
equal_label.grid(column = 0, row = 1)
result_label.grid(column = 1, row = 1)
miles_label.grid(column = 2, row = 0)
kilomet_label.grid(column = 2, row = 1)

#entry
convertor_input = Entry()
convertor_input.grid(column = 1, row = 0,)

#button
convertor_button = Button(text="Convert", command=convertclick)
convertor_button.grid(column = 1, row = 2)
window.mainloop()