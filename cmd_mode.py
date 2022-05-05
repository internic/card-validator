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

num = [int(x) for x in str(CARD_NUMBER)] # convert integers to list

# Calculate IIN (Issuer Identification Number) / BIN (Bank identification number)
eight = num[:8]
six = num[:6]

def bin_check(bintype): # eight for 8 digit BIN, six for six digit BIN
    return int("".join([str(i) for i in bintype]))

CARD_BIN = bin_check(six)

# Calculate MII (Major industry identifier)
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
# Card validation by Luhn Algorithm 

# ONLINE CHECKS
# Check internet connection
# Search online database for Card country
# Search online database for Card currency
# Search online database for Card Issuing Bank
# Search online database for Card Issuing Bank URL
# Search online database for Card Issuing Bank contacts