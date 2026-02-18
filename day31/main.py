import pandas
from pandas import *
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
random_word = {}

#read file-------------------------
try:
    data = read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def randomflashcard():
    #random_word = list(data_dict[random.randint(0, 102)].values())
    #random_word_value = random_word[0]
    #random_word_key = list(data_dict[random.randint(0, 102)].keys())
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data_dict)
    canvas.itemconfig(canvas_front_text, text=random_word["French"], fill="black")
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flipcard)


def flipcard():
    global random_word
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_front_text, text=random_word["English"], fill="white")


def is_known():
    data_dict.remove(random_word)
    data_leaned = pandas.DataFrame(data_dict)
    data_leaned.to_csv("data/words_to_learn", index=False)
    randomflashcard()

#UI---------------------------------

window = Tk()
window.title("Flasher")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flipcard)

canvas = Canvas(width=800, height=526)
canvas.grid(column=0, row=0, columnspan=2)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_bg = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_title = canvas.create_text(400,150, text="", font=("Arial", 40, "italic"))
#word function change
canvas_front_text = canvas.create_text(400, 263, fill="black", text="", font=("Arial", 60, "bold"))

correct_image = PhotoImage(file="images/right.png")
button_right = Button(image=correct_image, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=randomflashcard)
button_wrong.grid(row=1, column=0)




randomflashcard()
window.mainloop()
