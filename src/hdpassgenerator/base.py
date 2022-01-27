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

"""
    Convert bytes to bignum
"""
def bytes_to_bignum(_bytes):
    bignum = 0
    for (index, octet) in enumerate(_bytes[::-1]):
        bignum += octet * (256 ** index)
    
    return bignum

"""
    Convert bignum to base95
"""
def bignum_to_base95(_bignum):
    base95=""
    
    while _bignum != 0:
        base95 += chr(32 + _bignum % 95)
        _bignum = int(_bignum/95)

    return base95[::-1]

"""
    Convert bytes to base95
    _bytes -> i.e. sha256().digest()
"""
def bytes_to_base95(_bytes):
    bignum = bytes_to_bignum(_bytes)
    base95 = bignum_to_base95(bignum)
    return base95
