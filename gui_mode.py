#!/usr/bin/env python3

# PAYMENT CARD VALIDATOR GUI MODE
import requests

from requests import get
from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Toplevel, Canvas, Entry, Text, Button, PhotoImage, messagebox

#pyglet for custom fonts
#from pyglet import font

# GUI settings
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Using custom font didn't success because python couldn't import pyglet
#font.add_file(relative_to_assets("Inter-Regular.ttf"))
#Inter_Regular = font.load('Inter Regular')

# ---------------------------- GUI Mode --------------------------------- #
# Main Window
window = Tk()

window.geometry("645x327")
window.configure(bg = "#FFFFFF")

window.title("Payment Card Validator")

# validate button
def input_validation():
    pass

# help & info button
def help_info():
    
    # info window
    eula_info = Toplevel()
    eula_info.geometry("492x396")
    eula_info.configure(bg = "#FFFFFF")
    eula_info.title("Info & help")
    
    inf_canvas = Canvas(
        eula_info,
        bg = "#FFFFFF",
        height = 396,
        width = 492,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    inf_canvas.place(x = 0, y = 0)
    inf_canvas.create_text(
        45.0,
        92.0,
        anchor="nw",
        text="This software is a tool for checking the validity of Payment Card \nNumbers (PCN/PAN). Payment Cards are numbered in accordance with \nthe ISO/IEC 7812 Standard. The validity of Payment Cards is checked \nby a special algorithm for calculating the checksum, called the Luhn \nAlgorithm. This software provides the ability to check the numbers of \npotential Payment Cards for compliance with the Luhn Algorithm and \nalso calculates the following data:\n\nIssuer Identifier Number / Bank Identification Number\nMajor Industry Identifier\nCard Brand (Payment System I.E. Visa, Mastercard Etc.)\n\nUsing IIN/BIN Number, the following data is retrieved from a public database:\n\nCountry Of Issue Of Payment Card\nCurrency\nCard Issuing Bank\nIssuing Bank Contact Information (Website, Phone, Etc.)",
        fill="#060405",
        font=("Inter Regular", 12 * -1)
    )

    inf_canvas.create_text(
        45.0,
        31.0,
        anchor="nw",
        text="CARD \nVALIDATOR",
        fill="#060405",
        font=("Inter Black", 19 * -1)
    )
    
    image_decor_1 = PhotoImage(
        file=relative_to_assets("decor_1.png"))
    decor_1 = inf_canvas.create_image(
        336.0,
        21.0,
        image=image_decor_1
    )
    
    image_decor_2 = PhotoImage(
        file=relative_to_assets("decor_2.png"))
    decor_2 = inf_canvas.create_image(
        14.0,
        131.0,
        image=image_decor_2
    )
    eula_info.resizable(False, False)
    eula_info.mainloop()
    
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 327,
    width = 645,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=input_validation,
    relief="flat"
)
button_1.place(
    x=443.0,
    y=191.0,
    width=170.0,
    height=35.0
)