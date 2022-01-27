#!/usr/bin/env python3

from getpass import getpass

class Console:
    def __init__(self, wellcome):
        self.inform(wellcome)

    def clear(self):
        print("\033c\033[3J")

    """
        Print a message on screen
        message -> string  -  message to be printed
        new_page -> bool   -  clear console before print
    """
    def inform(self, message, new_page=True):
        if new_page:
            self.clear()
        else:
            print("")
        print(message)
        input("\n(press enter to continue)")

    """
        Request an input from user
        message  -> string -  input request
        secret   -> bool   -  hide input
        new_page -> bool   -  clear console before print
    """
    def read(self, message, secret=False, new_page=True):
        if new_page:
            self.clear()
        else:
            print("")
        print(message)
        if secret:
            return getpass(">> ")
        return input(">> ")
    
    def get_dbpassword(self):
        return self.read('Insert the database password:', True)