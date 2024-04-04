import sqlite3

# Create a connection to the database
con = sqlite3.connect('app.db')
cur = con.cursor()

# Create the 'category' table if it doesn't exist
cur.execute('''CREATE TABLE IF NOT EXISTS category(
               category_id INTEGER PRIMARY KEY,
               category_name TEXT NOT NULL
            )''')

# Insert data into the 'category' table
cur.execute('''INSERT INTO category(category_name)
               VALUES ('technology'),
                      ('e-commerce'),
                      ('gaming')
            ''')
            
# Update the category name
cur.execute('''UPDATE category SET category_name = 'online shop' 
               WHERE  category_id = 2''')

# Commit the changes to the database
con.commit()

# Fetch all categories and print them
categories = cur.execute("SELECT * FROM category").fetchall()
print(categories)

# Close the connection to the database
con.close()

