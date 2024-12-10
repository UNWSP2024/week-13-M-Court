#first program. write a program that displays the data from the cities database

import sqlite3

def main():

    #print greeting
    print("Displaying data from 'Cities' database...")

    #create connection with test database
    conn = sqlite3.connect("cities.db")
    #create cursor for modifying database
    cur = conn.cursor()

    #read from cities table
    cur.execute("SELECT * FROM Cities")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    #terminate connection with test database
    conn.close()

if __name__ == '__main__':
    main()
