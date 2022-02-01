# Hierarchical-Deterministic Password Generator
HDPasswordGenerator is a password generator and manager that offers a solution for recovering passwords on another machine if they are lost. The technique used for this is based on the bip32 and bip39 standards used in cryptocurrency wallets (described below) for the generation of deterministic and hierarchical keys.

#### Development Status -> Alpha

## Installation
### Compatibility
UNIX-like systems
### Install
    # Clone repository from github (--recursive is required to include submodules)
    git clone https://github.com/sebastiaoteixeira/HDPasswordGenerator.git --recursive
    cd HDPasswordGenerator
    
    # Install HDPasswordGenerator
    sudo python3 setup.py install

## Run
    hdpassgenerator

## Credits
- [ismailakkila](https://github.com/ismailakkila 'ismailakkila')
  - [BIP32 Implementation using Python](https://github.com/ismailakkila/bip32 'BIP32 Implementation using Python')