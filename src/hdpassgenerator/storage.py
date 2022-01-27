#!/usr/bin/env python3

from pysqlcipher3 import dbapi2 as sqlite

import os

HOME_DIR = os.path.expanduser('~')
DATA_DIR = os.path.join(HOME_DIR, '.hdpassgenerator') ## UNIX-like
WALLETS_DIR = os.path.join(DATA_DIR, 'wallets')


"""
    Get wallet list from .hdpassgenerator/wallets directory
"""
def get_wallet_list():
    return os.listdir(WALLETS_DIR)


"""
    Construct the wallets directory tree
"""
def create_directory_tree(wallet_name):
    path = DATA_DIR
    create_dir(path)

    path = DATA_DIR + '/wallets/'
    create_dir(path)
        
    path += '%s/' % (wallet_name)
    create_dir(path)


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


"""
    Create a new wallet database
    Tables:
        -> key - master key
        -> data - keys derivation data
"""
def create_wallet(name, password, key):
    conn=sqlite.connect(WALLETS_DIR + ('/%s/%s.db' % (name, name)))
    c = conn.cursor()
    c.execute("PRAGMA key='%s'" % (password))
    c.execute('CREATE TABLE key (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, private TEXT, derivation_path TEXT)')
    c.execute('CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user INTEGER, service TEXT, login TEXT, order_id INTEGER, derivation_path TEXT, length INTEGER)')
    c.execute("INSERT INTO key(private, derivation_path) VALUES ('%s', 'm')" % (key))
    conn.commit()
    c.close()
    return load_wallet(name, password)


def load_wallet(name, password):
    conn=sqlite.connect(WALLETS_DIR + ('/%s/%s.db' % (name, name)))
    c = conn.cursor()
    c.execute("PRAGMA key='%s'" % (password))
    c.execute("SELECT * FROM data")
    res = c.fetchall()
    conn.commit()
    c.close()
    return res


"""
    Saves a password metadata into database
"""
def save_data(name, password, user, service, login, order_id, derivation_path, length):
    derivation_path_str = 'm'
    for derivation in derivation_path:
        derivation_path_str += ('/' + str(derivation))
    conn=sqlite.connect(WALLETS_DIR + ('/%s/%s.db' % (name, name)))
    c = conn.cursor()
    c.execute("PRAGMA key='%s'" % (password))
    c.execute("SELECT * FROM data WHERE derivation_path='%s'" % (derivation_path_str))
    if (len(c.fetchall()) > 0):
        conn.commit()
        c.close()
        return
    c.execute("INSERT INTO data(user, service, login, order_id, derivation_path, length) VALUES (%d, '%s', '%s', %d, '%s', %d)" % (user, service, login, order_id, derivation_path_str, length))
    conn.commit()
    c.close()


"""
    Get master key from database
"""
def get_masterkey(name, password):
    conn=sqlite.connect(WALLETS_DIR + ('/%s/%s.db' % (name, name)))
    c = conn.cursor()
    c.execute("PRAGMA key='%s'" % (password))
    c.execute("SELECT private FROM key WHERE derivation_path='m'")
    masterkey = c.fetchone()[0]
    conn.commit()
    c.close()
    return masterkey


"""
    Verify if wallet database exists
    @return True if wallet database exists
"""
def wallet_exists(wallet_name):
    wpath = os.path.join(os.path.join(WALLETS_DIR, wallet_name), wallet_name + '.db')
    return os.path.exists(wpath)
