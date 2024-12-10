#second program
#write a program that allows the user to read, update and delete rows from the phone book database

#import SQL language
import sqlite3

#create main loop
def main():

    #connect with database
    conn = sqlite3.connect("cities.db")
    #create cursor
    cur = conn.cursor()

    #set again as y
    again = "y"

    #user actions
    while again == "y":
        # ask user what they would like to do
        user_answer = input("Type the number of the action you wish to take. \n 1. Read all rows \n 2. Add a row \n 3. Update a row \n 4. Delete a row \n ")

        #OPTION 1 ---- READ ALL ROWS
        if user_answer == "1":
            #print greeting
            print("Let's read all rows! ")

            #read rows
            cur.execute("SELECT * FROM cities")
            rows = cur.fetchall()
            #print rows
            for row in rows:
                print(row)

        #OPTION 2 --- ADD A ROW
        if user_answer == "2":
            #print greeting
            print("Let's add a new row!")

            #enter number
            new_country = input("Enter new city: ")
            new_pop = input("Enter its population: ")

            #insert user's city & population
            cur.execute('''INSERT INTO cities (CityName, Population) VALUES (?, ?)''', (new_country, new_pop))

        #OPTION 3---- UPDATE A ROW
        if user_answer == "3":

            #print greeting
            print("Let's update a row!")

            #get row ID
            user_id = input("Enter the row number: ")

            # enter number
            new_country = input("Enter a new city: ")
            new_pop = input("Enter its population: ")

            #change
            cur.execute('''UPDATE Cities SET CityName = ?, Population = ? WHERE CityID = ?''', (new_country, new_pop, user_id))

        #OPTION 4------ DELETE A ROW
        if user_answer == "4":
            #print greeting
            print("Let's delete a row!")

            user_id = input("enter the row ID: ")

            #delete table
            cur.execute("DELETE FROM Cities WHERE CityID = ?", (user_id,))

        #save changes
        conn.commit()

        #ask user to continue
        again = input("Type 'y' to complete another action. \n If not, type 'n'. ")

    #print exit greeting
    print("\nThank you for making changes! Bye!")

    #terminate connection
    conn.close()

#main loop
if __name__ == '__main__':
    main()

