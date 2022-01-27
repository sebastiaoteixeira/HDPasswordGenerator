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

from hashlib import sha3_224, sha3_256, sha3_512
from mnemonic import Mnemonic
from . import storage
from bip32 import Xkey
import pathlib
import sys
import os

"""
    LONG_MNEMONIC_SIZE = True  --->   24 words   RECOMMENDED
    LONG_MNEMONIC_SIZE = False --->   20 words
"""
LONG_MNEMONIC_SIZE = True


"""
    PasswordWallet class contains all
    necessary methods to generate,
    get and derivate keys
"""

class PasswordWallet():
    def __init__(self, name, lang="english"):
        self.name = name
        self.lang = lang
        self.mnem = Mnemonic(language=self.lang)
        self.filename = storage.WALLETS_DIR + ('/%s/%s.db' % (self.name, self.name))

    """
        Generate entropy from user input and system os.getrandom()
        TODO 64 characters counter
    """
    def get_random_input(self):
        input_random = ''
        first = 0
        while len(input_random) < 64: 
            if first == 1:
                console.inform('You have to enter 64 characters at minimum', False)
            input_random = console.read('Insert random characters to generate entropy:', True)
            first = 1
        
        ## Generate a random unicode string and add it to input_random
        random_unicode_str = input_random
        for i in [chr(int.from_bytes(os.getrandom(2), byteorder = sys.byteorder)) for i in range(64)]:
            random_unicode_str += i
        return random_unicode_str.encode('utf-8', "ignore")
    

    """
        Generate random words
        Get entropy from user input and system os.getrandom()
    """
    def generate_words(self):
        input_random = self.get_random_input()
        
        if LONG_MNEMONIC_SIZE:
            entropy = sha3_256(input_random).digest()
        else:
            entropy = sha3_224(input_random).digest()
        words = self.mnem.to_mnemonic(entropy)
        return words


    """
        Get master key from 24 + 1 words
    """
    def get_master_key(self, words: str, passphrase):
        seed = self.mnem.to_seed(words, passphrase=passphrase)
        master_key = Xkey.parse_from_seed(seed)
        return master_key
    

    """
        Generate a new random master key
    """
    def generate_master_key(self):
        words = self.generate_words()
        console.inform(words)
        passphrase = console.read('Insert extra word (leave blank for default):')
        return self.get_master_key(words, passphrase)


    """
        Create a new wallet
        @see storage.create_wallet()
    """
    def create_wallet(self):
        storage.create_directory_tree(self.name)
        dbpassword = console.get_dbpassword()
        if storage.wallet_exists(self.name):
            console.inform("This wallet already exists")
            return False
    
        master_key = self.generate_master_key()
        self.wallet_data = storage.create_wallet(self.name, key=master_key.serialize(), password=dbpassword)

        return True


    """
        Recover a wallet from mnemonic
    """
    def recover_wallet(self):
        storage.create_directory_tree(self.name)
        dbpassword = console.get_dbpassword()
        if storage.wallet_exists(self.name):
            console.inform("This wallet already exists")
            return False

        words = console.read('Insert the 24 words mnemonic:')
        passphrase = console.read('Insert extra word (leave blank if none):')
        master_key = self.get_master_key(words, passphrase)
        self.wallet_data = storage.create_wallet(self.name, key=master_key.serialize(), password=dbpassword)

        return True


    """
        Load wallet data
    """
    def load_wallet(self):
        while(True):
            dbpassword = console.get_dbpassword()
            if not storage.wallet_exists(self.name):
                console.inform("Name or password incorrect")
                continue
            self.wallet_data = storage.load_wallet(self.name, password=dbpassword)
            return


    """
        Derivate a child key from master key
        @param derivation_path -> list (5 expected elements)
        @param dbpassword      -> string
    """
    def get_key(self, derivation_path, dbpassword):
        masterkey = Xkey.parse_from_bip32(storage.get_masterkey(self.name, dbpassword))
        derivation_path = [[i, False] for i in derivation_path]
        key = masterkey.derive_path(derivation_path)
        return key


    """
        Derivate an hash from a msg with a key
        @param msg             -> string
        @param derivation_path -> list (5 expected elements)
        @param dbpassword      -> string
        @return 512-bits hash
    """
    def derivate_from_msg(self, msg: str, derivation_path: list, dbpassword: str):
        key = self.get_key(derivation_path, dbpassword)
        hashed_msg = sha3_512(msg.encode('utf-8')).digest()
        hashed_key = sha3_512(key.serialize().encode('utf-8')).digest()
        root = sha3_512(hashed_msg + hashed_key).digest()
        return root


def define_console(_console):
    global console
    console = _console
