import tkinter

import pandas as pd
import numpy as np
from tkinter import *

# read the Excel file
df_sheet_index = pd.read_excel('Players_for_08-31-2022.xlsx')

# get the number of rows
rows = df_sheet_index.shape[0]

# get the index of the winner
index = np.random.randint(0, rows)


def fillWinnerInfo():
    # Start making the template
    canvas.create_text(300, 30, text="Winner", font="Arial 16 italic", fill="red")
    canvas.create_text(75, 100, text="Index: ", font="Arial 16 italic", fill="blue")
    canvas.create_text(75, 140, text="Winner: ", font="Arial 16 italic", fill="blue")
    canvas.create_text(75, 180, text="Play on: ", font="Arial 16 italic", fill="blue")
    canvas.create_text(75, 220, text="Discord: ", font="Arial 16 italic", fill="blue")
    y = 100
    # Write each info of the selected person
    for i in range(0, 4):
        canvas.create_text(300, y, text=df_sheet_index.iloc[index][i], font="Arial 16 italic", fill="blue")
        y = y + 40


# Creation of the window
window = Tk()
window.title("Lottery")

# Make a drawing stylesheet
canvas = Canvas(window, width=600, height=300, background='yellow')

# Fill the info with the winner
fillWinnerInfo()

# Organize widgets as blocks before placing them
canvas.pack()

# Launch the window
window.mainloop()
