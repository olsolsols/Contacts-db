import sqlite3



#create or open a database called c2Music.db
conn = sqlite3.connect('c2Music.db')
cursor = conn.cursor()

def showRecords():
    cursor.execute('SELECT * FROM members')
    row = cursor.fetchall()
    for record in row:
        print(record)
# showRecords()

#main.po
# readMembers.showRecords