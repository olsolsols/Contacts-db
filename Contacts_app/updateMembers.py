import sqlite3

import time

#create or open a database called c2Music.db
conn = sqlite3.connect('c2Music.db')
cursor = conn.cursor()

def update():
    #enter id of record to be updated
    keyField = input("Enter ID of the record to be updated: ")
    #enter the field name to be updated
    field = input("Which field you want to update: (Firstname, Lastname, Email): ")
    #field value 
    newFieldValue = input("Enter the new value for the field you are updating: ")
    print(newFieldValue)

    #Update members set fieldname = 'fieldValue'
    newFieldValue = "'" + newFieldValue + "'"
    print(newFieldValue)
    # newFieldValue = " + newFieldValue + "
    # print(newFieldValue)

    try:
        #set field = Firstname, Lastname, Email and Value = newFieldValue, where memberid = 1
        cursor.execute("UPDATE members SET " + field + "=" + newFieldValue + " WHERE MemberID" + "=" + keyField)
        conn.commit()
        print("Member Updated")

        time.sleep(2)
        cursor.execute('SELECT * FROM members')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Record not updated")
# update()