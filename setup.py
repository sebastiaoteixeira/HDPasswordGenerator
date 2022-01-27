#!/usr/bin/env python3
from setuptools import setup
import requests
import os

print()
# Download rockyou list
url = 'https://gateway.pinata.cloud/ipfs/QmPvcDGMmq6CPGAAQHhGfpp6XQdqTV7SqhbZPhCDwDrVcF/rockyou.txt'
myfile = requests.get(url)
open(os.path.dirname(os.path.join(os.path.abspath(__file__), 'src/hdpassgenerator/rockyou.txt')), 'wb').write(myfile.content)


setup(
    name="hdpassgenerator",
    version="0.1.0",
    author="Sebastião Teixeira",
    description="Hierarchical Deterministic Password Generator",
    packages=["hdpassgenerator"],
    package_dir={"": "src"},
    package_data={
        "": ["wordlist/rockyou.txt"],
        "": ["bip32/*"]
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
        "License :: OSI Approved :: GPL3 License",
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