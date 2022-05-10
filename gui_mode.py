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