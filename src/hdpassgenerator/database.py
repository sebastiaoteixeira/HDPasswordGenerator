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