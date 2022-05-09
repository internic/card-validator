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
def card_brand():
    # Brands Database
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

    matches = []
        for key, value in brands_database.items():
            for item in value:
                if card.startswith(str(item)):
                    matches.append(item)
                else:
                    matches.append(0)
        
        for key, value in brands_database.items():
            for item in value:
                if item == max(matches):
                    return key
                else:
                    return "Not found"

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

if check_luhn():
    print(f"Card number {CARD_NUMBER} is valid \nIIN/BIN number: {CARD_BIN} \nCard industry: {INDUSTRY} \nCard Brand: {BRAND} \n")

    # -----------------------------  ONLINE CHECKS ------------------------------ #
    
    # check internet connection
    def connection_check():
        url='http://www.google.com/'
        timeout=5
        try:
            net = requests.get(url, timeout=timeout)
            return True
        except requests.ConnectionError:
            print("Internet connection error")
        return False
    
    if connection_check():  
        try:
            cardinfo = get(f"https://lookup.binlist.net/{CARD_BIN}", headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', "Accept-Version": "3"}).json()
            
            card_country = card_currency = card_bank = bank_url = bank_phone = "Not found"
            
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



# Check internet connection
# Search online database for Card country
# Search online database for Card currency
# Search online database for Card Issuing Bank
# Search online database for Card Issuing Bank URL
# Search online database for Card Issuing Bank contacts