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
i = 0

def forward_items():
    global i
    canvas.itemconfig(language_label, text= language_list[i])
    canvas.itemconfig(word_label, text = word_list[i])
    i+=1
    print(i)
def backward_items():
    global i

    canvas.itemconfig(language_label, text=language_list[i])
    canvas.itemconfig(word_label, text=word_list[i])
    i-=1

    print(i)
#-----------------UI SET UP-----------#
#images
check_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_image = PhotoImage(file="images/card_front.png")

#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness= 0)
canvas.create_image(400,263,image = card_image)
language_label = canvas.create_text(400,150, text="language", font= ("Ariel,",40,"italic"))
word_label =canvas.create_text(400,263, text= "word", font= ("Ariel,",60,"bold"))
#buttons
check_button = Button(image= check_image, highlightthickness= 0, command= forward_items)
wrong_button = Button(image= wrong_image, highlightthickness= 0, command= backward_items)

#positioning
canvas.grid(column = 0, columnspan = 2, row = 0)
check_button.grid(column = 0, row = 1)
wrong_button.grid(column = 1, row = 1)


window.mainloop()