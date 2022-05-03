from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_random_word = {}
new_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    all_words = pandas.read_csv("data/french_words.csv")
    new_dict = all_words.to_dict(orient="record")
else:
    new_dict = data.to_dict(orient="record")


def next_card():
    global set_timer, current_random_word
    window.after_cancel(set_timer)
    current_random_word = random.choice(new_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_random_word["French"], fill="black")
    canvas.itemconfig(card_backround, image=card_front_img)
    set_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_random_word
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_random_word["English"], fill="white")
    canvas.itemconfig(card_backround, image=card_backround_img)


def is_known():
    new_dict.remove(current_random_word)
    print(len(new_dict))
    df = pandas.DataFrame(new_dict)
    df.to_csv("data/words_to_learn.csv")
    next_card()



window = Tk()
window.title("Flash Card Project")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.grid()

set_timer = window.after(3000, func=flip_card)
# images
card_front_img = PhotoImage(file="images/card_front.png")
true_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
card_backround_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_backround = canvas.create_image(400, 273, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
# canvas.create_image(0, 0, image=right_img)
wrong_button = Button(image=wrong_img, command=next_card)
wrong_button.grid(row=1, column=0)
true_button = Button(image=true_img, command=is_known)
true_button.grid(row=1, column=1)

next_card()

window.mainloop()



