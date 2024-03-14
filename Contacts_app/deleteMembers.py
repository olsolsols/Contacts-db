import sqlite3

import time

#create or open a database called c2Music.db
conn = sqlite3.connect('c2Music.db')
cursor = conn.cursor()

# keyfield = keyfield + keyfield
def delRecord():
    keyField=input("Enter ID of record to be delted: ")
    try:
        cursor.execute("DELETE FROM members WHERE MemberID=" + keyField)
        conn.commit()
        print("\Record deleted")

        time.sleep(2)
        cursor.execute('SELECT * FROM members')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Record not deleted")

def showRecords():
    searchID = input("Enter ID of of record to search for: ")

    cursor.execute('SELECT * FROM members WHERE MemberID='+ searchID)
    row = cursor.fetchall()
    for record in row:
        print(record)


# showRecords()

# delRecord()