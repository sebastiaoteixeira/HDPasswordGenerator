#!/usr/bin/env python3
#
# Hierarchical Deterministic Password Generator
# Copyright (C) 2022 Sebastião Teixeira
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
