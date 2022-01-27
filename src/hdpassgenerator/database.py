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

from pysqlcipher3 import dbapi2 as sqlite

def save(wallet):

    conn=sqlite.connect('/home/tiao/.hdpassgenerator/wallets/main/main1.db')
    c = conn.cursor()
    c.execute("PRAGMA key='pass'")
    c.execute('create table stocks (date text, trans text, symbol text, qty real, price real)')
    c.execute("insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)")
    conn.commit()
    c.close()
    
run()
