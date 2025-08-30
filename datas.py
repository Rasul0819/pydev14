import sqlite3


db = sqlite3.connect('tgbot.db')

cursor = db.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               id INTEGER,
               name TEXT, 
               phone_number TEXT,
               address TEXT)

''')
db.commit()

async def save_user(id,name,phone_num,adres):
    cursor.execute('''
INSERT INTO users(
                   id,name,phone_number,address)
                   VALUES(?,?,?,?)

''',(id,name,phone_num,adres))
    db.commit()

async def show_users():
    cursor.execute('SELECT * FROM users')
    datas = cursor.fetchall()
    return datas