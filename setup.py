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

from setuptools import setup
import requests
import os

# Download rockyou list
print("Downloading...\nIt may take a few minutes")
url = 'https://gateway.pinata.cloud/ipfs/QmPvcDGMmq6CPGAAQHhGfpp6XQdqTV7SqhbZPhCDwDrVcF/rockyou.txt'
rockyou = requests.get(url)
open(__file__[:(len(__file__)-8)] + 'src/hdpassgenerator/wordlist/rockyou.txt', 'wb').write(rockyou.content)


setup(
    name="hdpassgenerator",
    version="1.0.0",
    author="Sebastião Teixeira",
    description="Hierarchical Deterministic Password Generator",
    packages=["hdpassgenerator"],
    package_dir={"": "src"},
    package_data={
        "": ["wordlist/rockyou.txt"]
    },
    entry_points={
        'console_scripts': [
            'hdpassgenerator=hdpassgenerator:run'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
    ],
)

setup(
    name="bip32",
    version="1",
    author="ismailakkila",
    packages=["bip32"],
    package_dir={"": "lib"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
    ],
)
