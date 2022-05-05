#!/usr/bin/env python3

# PAYMENT CARD VALIDATOR CMD MODE Version 0.01
import requests
from requests import get

# OFFLINE CHECKS
# Get user input (card number), and check errors (input validation)
def input_validation():
    
    # initital
    card_num = "testnum"
    in_range = False
    
    while card_num.isdigit() == False or in_range == False or int(card_num) == 0:
        # get user input and remove spaces
        card_num = input("Please enter payment card number (11-19 digits): ").replace(" ", "")
           
        # digit check
        if card_num.isdigit() == False:
            print("Sorry your input is not a digit!")
            
        # range check
        if card_num.isdigit() == True:
            if len(card_num) >= 11 and len(card_num) <= 19:
                in_range = True
            else:
                print("You are out of range (11-19 digits)")
                in_range == False
                
    return int(card_num)

CARD_NUMBER = input_validation()

# Calculate IIN (Issuer Identification Number) / BIN (Bank identification number)
eight = num[:8]
six = num[:6]

def bin_check(bintype): # eight for 8 digit BIN, six for six digit BIN
    return int("".join([str(i) for i in bintype]))

CARD_BIN = bin_check(six)

# Calculate MII (Major industry identifier)
# Calculate Card Brand (Visa, MasterCard, Maestro, etc.)
# Card validation by Luhn Algorithm 

# ONLINE CHECKS
# Check internet connection
# Search online database for Card country
# Search online database for Card currency
# Search online database for Card Issuing Bank
# Search online database for Card Issuing Bank URL
# Search online database for Card Issuing Bank contacts