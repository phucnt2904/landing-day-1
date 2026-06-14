# -*- coding: utf-8 -*-
import sqlite3

DB = r"d:\AI91\landing-day-1\brain.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("PRAGMA table_info(products)")
cols = [r[1] for r in cur.fetchall()]
if "quantity" not in cols:
    cur.execute("ALTER TABLE products ADD COLUMN quantity INTEGER DEFAULT 0")
    # seed a default quantity: con_hang -> 10, het_hang -> 0
    cur.execute("UPDATE products SET quantity = 10 WHERE stock_status = 'con_hang'")
    cur.execute("UPDATE products SET quantity = 0 WHERE stock_status = 'het_hang'")
    print("Added quantity column to products")

cur.execute("PRAGMA table_info(orders)")
cols = [r[1] for r in cur.fetchall()]
if "quantity" not in cols:
    cur.execute("ALTER TABLE orders ADD COLUMN quantity INTEGER DEFAULT 1")
    print("Added quantity column to orders")

conn.commit()
conn.close()
print("done")
