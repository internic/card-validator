#!/usr/bin/env python3

# PAYMENT CARD VALIDATOR CMD MODE Version 0.01
import requests
from requests import get

# OFFLINE CHECKS
# Get user input (card number), and check errors (input validation)
# Calculate IIN (Issuer Identification Number) / BIN (Bank identification number)
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