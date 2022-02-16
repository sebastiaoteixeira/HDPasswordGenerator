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

from . import generator
from .console import Console
from . import wallet
from . import storage


"""
    Starts here
"""
def run():
    init_console()

    wlt = wallet_menu()
    password_menu(wlt)

    return


def wallet_menu():
    success = False
    while (not success):
        action = int(console.read("Choose action:\n\n0 -> Create a new passwords wallet\n1 -> Open a passwords wallet\n2 -> Recover a passwords wallet\n"))

        if (action == 0 or action == 2): 
            wallet_name = console.read("Insert the wallet name:")
        elif (action == 1):
            wallet_name = console.read("Available Wallets:\n -> " + "\n -> ".join(storage.get_wallet_list()) + "\n\nInsert the wallet name:")
        else:
            console.inform("Invalid action. Try again.")
            return run()

        wlt = wallet.PasswordWallet(wallet_name)

        if (action == 0):
            success = wlt.create_wallet()
        elif (action == 1):
            success = wlt.load_wallet()
        elif (action == 2):
            success = wlt.recover_wallet()
    return wlt

"""
    Go to passwords menu
    @param wlt -> PasswordWallet()
"""
def password_menu(wlt):
    read = int(console.read("Choose action:\n\n0 -> Generate a new password\n1 -> Read passwords\n2 -> Change wallet\n3 -> Exit\n"))

    if (read == 0):
        password_gen = generator.PasswordGenerator(wlt)
        service = console.read("Service (i.e. example.org):")
        login = console.read("Account Login (i.e. user123):", new_page=False)
        password_length = console.read("Password Length (Leave blank for RECOMMENDED default [15]):", new_page=False)
        password_length = 15 if password_length == "" else int(password_length)
        password = password_gen.generate_valid_password(0, service, login, 0, password_length)
        console.inform("\n    " + password)
    elif (read == 1):
        pass
    elif (read == 2):
        run()
        return
    elif (read == 3):
        return

    password_menu(wlt)


"""
    Init console in all modules
"""
def init_console():
    message = "HIERARCHICAL-DETERMINISTIC PASSWORD GENERATOR\nBy Sebastião Teixeira"

    global console
    console = Console(message)
    wallet.define_console(console)
    generator.define_console(console)
