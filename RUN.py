#!/usr/bin/env python3

# PAYMENT CARD VALIDATOR RUN FILE
APP_MODE = input("TYPE 'c' TO RUN IN COMMAND-LINE MODE, TYPE 'g' FOR GUI MODE OR ANY OTHER KEY TO EXIT THE APP: \n")

if APP_MODE == "c":
    # run CMD Mode file
    import cmd_mode

elif APP_MODE == "g":
    # run GUI Mode file
    import gui_mode
else:
    # quit the app
    print("Quitting...")