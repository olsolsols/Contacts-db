import sqlite3

import time

#create or open a database called c2Music.db
conn = sqlite3.connect('c2Music.db')
cursor = conn.cursor()
#create a subroutine and add members
def addMembers():
    # CREATE AN EMPTY LIST members
    members = []
    #memberID field is autoincremented

    fname = input("Enter your first name: ")
    lname = input("Enter your lastname: ")
    email = input("Enter your email: ")

    members.append(fname)
    members.append(lname)
    members.append(email)

    try: 
        cursor.execute('INSERT INTO members VALUES (NULL, ?, ?, ?)', members)
        conn.commit()
        print("Member Added")

        time.sleep(2)
        cursor.execute('SELECT * FROM members')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("record not added")

#addMembers()
