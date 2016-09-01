import sqlite3

def find_details(id2find):
    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if row['ID'] == id2find:
#create a hash
            s = {}
#associate each value in the hash to a row in the database, converted to a string
            s['ID'] = str(row['id'])
            s['name'] = str(row['name'])
            s['country'] = str(row['country'])
            s['average'] = str(row['average'])
            s['board'] = str(row['board'])
            s['age'] = str(row['age'])
            cursor.close()
            return(s)
    cursor.close()
    return({})

lookup_ID = int(input("Enter the ID of the surfer: "))
surfer = find_details(lookup_ID)
if surfer:
    # display in the format below
    print("ID: " + surfer['ID'])
    print("Name:    " + surfer['name'])
    print("Country: " + surfer['country'])
    print("Average: " + surfer['average'])
    print("Board:   " + surfer['board'])
    print("Age:     " + surfer['age'])
