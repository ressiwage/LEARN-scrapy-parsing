import sqlite3
#Connecting to sqlite
conn = sqlite3.connect('data.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS news")
#Creating table as per requirement
sql ='''CREATE TABLE news(
   title text NOT NULL,
   body text,
   creation datetime
)'''
cursor.execute(sql)
print("Table created successfully........")

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()