from tkinter import *
from tkinter import messagebox
import pandas
import random

#constants
BACKGROUND_COLOR = "#B1DDC6"
#GUI set up
window = Tk()
window.title("flashcards")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)


#------------LOGIC-------------#
data = pandas.read_csv("data/japanese_words.csv")
data_dict = dict(zip(data['Japanese'], data['English']))
language_list = [key for key in data_dict.keys()]
word_list = [value for value in data_dict.values()]
known_list = [] #this will be appended too when someone clicks the check button
i = 0
is_flipped = False
def changecard():
    global i, is_flipped
    if not is_flipped:
        canvas.itemconfig(language_label, text="Japanese")
        canvas.itemconfig(word_label, text=language_list[i])
        canvas.itemconfig( canvas_image, image=card_image)
    else:
        canvas.itemconfig(canvas_image, image=back_image)
        canvas.itemconfig(language_label, text="English")
        canvas.itemconfig(word_label, text=word_list[i])
    is_flipped = not is_flipped

    # Schedule the next flip in 3000 ms
    window.after(3000, changecard)

# CHECK IF CAN DO THIS WITH ITTERROWS!!!
def forward_items():
    global i

    canvas.itemconfig(word_label, text = language_list[i +1])
    item = language_list.pop(i)
    known_list.append(item)
    print(known_list)
    print(language_list)
    i+=1


    print(i)

def backward_items():
    global i
    if i < 0:
        canvas.itemconfig(word_label, text= language_list[0])
        switch = 0
    elif i>0:
        canvas.itemconfig(word_label, text=language_list[i - 1])
        i-=1
        switch = 0
    print(i)

#-----------------UI SET UP-----------#
#images
check_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness= 0)
canvas_image =canvas.create_image(400,263,image = card_image)
language_label = canvas.create_text(400,150, text="Japanese", font= ("Ariel,",40,"italic"))
word_label =canvas.create_text(400,263, text= language_list[0], font= ("Ariel,",60,"bold"))
#buttons
check_button = Button(image= check_image, highlightthickness= 0, command= forward_items)
wrong_button = Button(image= wrong_image, highlightthickness= 0, command= backward_items)

#positioning
canvas.grid(column = 0, columnspan = 2, row = 0)
check_button.grid(column = 0, row = 1)
wrong_button.grid(column = 1, row = 1)



changecard()
window.mainloop()