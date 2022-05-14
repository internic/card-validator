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
    
    #print("Validate button clicked")
    if len(entry_1.get()) >= 11 and int(entry_1.get()) != 0:

        global CARD_NUMBER
        CARD_NUMBER = entry_1.get()

        num = [int(x) for x in str(CARD_NUMBER)] # convert integers to list

        # Calculate IIN (Issuer Identification Number) / BIN (Bank identification number)
        eight = num[:8]
        six = num[:6]     
        
        # Calculate Card BIN number
        def bin_check(bintype): # eight for 8 digit BIN, six for six digit BIN
            return int("".join([str(i) for i in bintype]))

        CARD_BIN = bin_check(six)

        # Major industry identifier
        def mii_check():
            mii_base = {"ISO/TC 68 and other industry assignments": 0,
                        "Airlines": 1,
                        "Airlines, financial and other future industry assignments": 2,
                        "Travel and entertainment": 3,
                        "Banking and financial.": 4,
                        "Banking and financial": 5,
                        "Merchandising and banking/financial": 6,
                        "Petroleum and other future industry assignments": 7,
                        "Healthcare, telecommunications and other future industry assignments": 8,
                        "For assignment by national standards bodies": 9}

            for key, value in mii_base.items():
                if num[0] == value:
                    return key

        INDUSTRY = mii_check()

        # Calculate Card Brand (Visa, MasterCard, Maestro, etc.)
        def card_brand():
            
            brands_database = {"American Express": [34,37],
                            "China T-Union": [31],
                            "China UnionPay": [62],
                            "Diners Club International": [36], 
                            "Diners Club United States & Canada": [54],
                            "Discover Card": [6011,65]+list(range(644,650)),
                            "Discover Card & China UnionPay co-branded": list(range(622126,622926)),
                            "UkrCard": list(range(60400100,60420100)),
                            "RuPay": [60,65,81,82,508],
                            "RuPay-JCB co-branded": [353,356],
                            "InterPayment": [636],
                            "InstaPayment": [637,638,639],
                            "JCB": list(range(3528,3590)),
                            "Laser": [6304, 6706, 6771, 6709],
                            "Maestro UK": [6759, 676770, 676774],
                            "Maestro": [5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763],
                            "Dankort": [5019],
                            "Dankort & Visa co-branded": [4571],
                            "Mir": list(range(2200,2205)),
                            "NPS Pridnestrovie": list(range(6054740,6054745)),
                            "MasterCard": list(range(2221,2721))+list(range(51,56)),
                            "Troy": [65, 9792],
                            "Visa": [4],
                            "Visa Electron": [4026, 417500, 4508, 4844, 4913, 4917],
                            "UATP": [1],
                            "Verve": list(range(506099,506199))+list(range(650002,650028)),
                            "LankaPay": [357111],
                            "UzCard": [8600],
                            "Humo": [9860],}
            
            card = str(CARD_NUMBER)
            
            matches = [-1]
            for key, value in brands_database.items():
                for item in value:
                    if card.startswith(str(item)):
                        matches.append(item)
                    else:
                        pass
            
            for key, value in brands_database.items():
                for item in value:
                    if item == max(matches):
                        return key
                    else:
                        pass

        BRAND = card_brand()
        
        # Card validation by Luhn Algorithm 
        def check_luhn():
            odd_digs = num[-1::-2] # reversed digits from the end with step 2
            even_digs = num[-2::-2] # reversed digits from the end+1 with step 2

            odd_summ = 0
            odd_summ = odd_summ + sum(odd_digs)

            # we multiply each item in reversed_even_digits_list by 2, joining the digits, and converting it into integers
            evensplitted = int("".join(map(str, [i * 2 for i in even_digs])))
            
            # we add integers to list and take sum of them
            even_summ = sum([int(a) for a in str(evensplitted)])
            
            return (odd_summ + even_summ) % 10 == 0  # if sum of the numbers mod 10 is equal to 0 the card is valid
            
        # Default status for online based variables
        card_country = card_currency = card_bank = bank_url = bank_phone = "Not found"
           
        if check_luhn():
            STATUS = f"{CARD_NUMBER} IS VALID"
            
            # --------------------------- Online checks ------------------------------ #
            
            # check internet connection
            def connection_check():
                url='http://www.google.com/'
                timeout=5
                try:
                    net = requests.get(url, timeout=timeout)
                    return True
                except requests.ConnectionError:
                    messagebox.showerror("Connection Error", "Internet connection error")
                return False
            
            if connection_check():
                try:
                    cardinfo = get(f"https://lookup.binlist.net/{CARD_BIN}", headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', "Accept-Version": "3"}).json()
                    
                    try:
                        card_country = cardinfo["country"]["name"]
                    except:
                        pass

                    try:
                        card_currency = cardinfo["country"]["currency"]
                    except:
                        pass

                    try:
                        card_bank = cardinfo["bank"]["name"]
                    except:
                        pass

                    try:
                        bank_url = cardinfo["bank"]["url"]
                    except:
                        pass

                    try:
                        bank_phone = cardinfo["bank"]["phone"]
                    except:
                        pass
                except:
                    messagebox.showerror("Database Error", "Error searching online database. Make sure your input is correct")
                    #print("Error searching online database. Make sure your input is correct")
            else:
                pass
                #print("Check your connection and try again")

        else:
            STATUS = f"{CARD_NUMBER} IS NOT VALID \nOR IT IS NOT GENERATED BY LUHN ALGORITHM"

        # --------------------------------- Validate Button Window ------------------------------ #

        validate_window = Toplevel()   # Tk() for main window Toplevel() for subwindow
        validate_window.geometry("492x315") # initial window size before more info button click 492x315
        validate_window.configure(bg = "#FFFFFF")
        validate_window.title("Card Validation")



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

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=help_info,
    relief="flat"
)
button_2.place(
    x=443.0,
    y=242.0,
    width=170.0,
    height=35.0
)

canvas.create_text(
    443.0,
    102.0,
    anchor="nw",
    text="ENTER YOUR CARD NUMBER:",
    fill="#060405",
    font=("Inter Regular", 12 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    223.0,
    163.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    528.0,
    150.5,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=448.0,
    y=137.0,
    width=160.0,
    height=29.0
)

canvas.create_text(
    443.0,
    31.0,
    anchor="nw",
    text="CARD \nVALIDATOR",
    fill="#060405",
    font=("Inter Black", 19 * -1)
)

# GUI mode input isdigit validation
def check_input(inp):
    if inp.isdigit() and len(inp) <= 19:
        return True
    elif inp == "":
        return True
    else:
        return False

digit_validation = window.register(check_input)
entry_1.config(validate="key", validatecommand=(digit_validation, "%P"))

window.resizable(False, False)
window.mainloop()

# ----------------------------------------------------------------------- #