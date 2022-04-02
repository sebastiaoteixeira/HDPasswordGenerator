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

from hashlib import sha3_224, sha3_512
from . import storage
from . import base
import os

class PasswordGenerator:
    def __init__(self, wallet):
        self.wallet = wallet
    
    """
        Validate Derivation Path
        It should have 5 elements 
    """
    def validate_derivation_path(self):
        if (len(self.derivation_path) == 5):
            Exception("Invalid derivation path")

        for derivation in self.derivation_path:
            if (not type(derivation) == int) or (derivation >= 2**16):
                Exception("Invalid derivation path")

    """
        Calculate a deterministic derivation index from a text message
    """
    def get_derivation_index(self, msg):
        derivation = sha3_224(msg.encode('utf-8')).digest()[:2]
        derivation = base.bytes_to_bignum(derivation)
        return derivation

    """
        Verify if password is valid
    """
    def is_password_valid(self, password, length):
        # Minimum Length - 50
        if (len(password) < 50):
            return False

        password = password[:length]

        # First/Last character cannot be a space
        if (password[0] == " " or password[(len(password)-1)] == " "):
            return False

        # Verify if exists lower case and upper case letters, numbers and symbols
        has_lower = False
        has_upper = False
        has_number = False
        has_symbol = False
        for c in password:
            if (c >= 'a' and c <= 'z'):
                has_lower = True
            elif (c >= 'A' and c <= 'Z'):
                has_upper = True
            elif (c >= '0' and c <= '9'):
                has_number = True
            else:
                has_symbol = True
        if not (has_lower and has_upper and has_number and has_symbol):
            return False

        # Rockyou Proof Test
        rockyou = open(os.path.dirname(os.path.abspath(__file__)) + '/wordlist/rockyou.txt', 'r', encoding='latin-1')
        if password in rockyou:
            return False

        return True
    
    """
        Construct all the derivation path and generate a valid password
        user    -> Reserved for future multi-user feature
        service -> Service string (URL) 
        account -> Service account login
    """
    def generate_valid_password(self, user, service, account, order_id, length):
        msg = service + account

        self.derivation_path = []
        self.derivation_path.append(user)                                  ## Reserved for multi-user wallet
        self.derivation_path.append(self.get_derivation_index(service))
        self.derivation_path.append(self.get_derivation_index(account))
        self.derivation_path.append(order_id)

        dbpassword = console.get_dbpassword()

        valid_password_derivation = 0
        while True:
            self.derivation_path.append(valid_password_derivation)
            password = self.generate_hash(msg, dbpassword)
            if self.is_password_valid(password, length):
                break

            self.derivation_path.pop(len(self.derivation_path) - 1)
            valid_password_derivation += 1
        
        storage.save_data(self.wallet.name, dbpassword, user, service, account, order_id, self.derivation_path, length)
        self.wallet.load_wallet(dbpassword)
        return password[:length]

    """
        Computes the sig key from master key through derivation path
        length  -> Number of characters to show
        Returns a strong password
    """
    def generate_hash(self, msg, dbpassword):
        self.validate_derivation_path()

        password_bytes = self.wallet.derivate_from_msg(msg, self.derivation_path, dbpassword)
        password = base.bytes_to_base95(password_bytes)
        return password


def define_console(_console):
    global console
    console = _console
