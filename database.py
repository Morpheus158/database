import psycopg2

def create_table():
    con = psycopg2.connect("dbname='postgres' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()

def insert(item, quantity, price):
    con = psycopg2.connect("dbname='postgres' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    con.commit()
    con.close()

def view():
    con = psycopg2.connect("dbname='postgres' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    con.close()
    return rows

def delete(item):
    con = psycopg2.connect("dbname='postgres' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item, ))
    con.commit()
    con.close()

def update(quantity, price, item):
    con = psycopg2.connect("dbname='postgres' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    con.commit()
    con.close()

create_table()
update(7,78.7,"Pacman board game")
#delete("Pacman board game")
#insert("Pacman board game", 14, 53.5)
print(view())
