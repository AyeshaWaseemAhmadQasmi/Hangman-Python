from tkinter import *
import random


#btn.grid(column = 1, row = 1)

remaining = 6
def guess():
    global remaining
    global spaces
    global label3
    global label4
    if remaining > -1 and spaces != code_word:
        #label4.config(text=spaces)
        #print(spaces)
        #print(spaces).set()
        #print(str(remaining)).set()
        #label4.config(text=str(remaining))
        guess_word = e.get()
        if len(guess_word) != 1:
            label3.config(text="Guess Word should be of one character only")
            #print("Guess Word should be of one character only").set()
        elif guess_word in code_word:
            label3.config(text="Gussed Character is in the code word!")
            #print("Gussed Character is in the code word!").set()
            spaces = fill_spaces(code_word, spaces, guess_word)
        else:
            label3.config(text="Guess Word is not in the code word")
            #print("Guess Word is not in the code word").set()
            remaining = remaining - 1
    

    elif remaining < 0:
        label3.config(text="You lost the game. The code was: " + str(code_word))
        #print("You lost the game. The code was: " + str(code_word)).set()
    else:
        label3.config(text="You lost the game. The code was: " + str(code_word))
        #print("Congratulations! You won the game.").set()
    label4.config(text=spaces)


def fill_spaces(code, curr_space, character):
    new = ""
    for i in range(len(code)):
        if code[i]==character:
            new = new + character

        else:
            new = new + curr_space[i]
    return new

#btn = Button(root, text = "Submit", command = guess()
#btn.grid(column = 1, row = 1)


root = Tk()
root.title("Hangman")
root.geometry("300x300")
label1=Label(root, text = "Guess a word", fg="black").pack()
label2=Label(root, text = "Enter a letter").pack()
e=Entry(root)
e.pack()
btn = Button(root, text = "Submit", command=guess)
btn.pack()
label4=Label(root, text="")
label4.pack()
label3=Label(root, text="")
label3.pack()
codes=["aeroplane", "computer", "snakes","apple","pakistan","spy"]
code_word = random.choice(codes)
spaces = "-" * len(code_word)
#guess()
root.mainloop()
