#!/usr/bin/env python3

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