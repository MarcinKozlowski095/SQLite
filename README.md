# Database Management with SQLite

This script demonstrates basic database management using SQLite in Python. It creates a database named `app.db` and performs operations such as table creation, data insertion, and data update.

## Code Description

1. **Database Connection**: Establishes a connection to the SQLite database named `app.db`.

2. **Table Creation**: Creates a table named `category` if it doesn't already exist. The table has two columns: `category_id` and `category_name`.

3. **Data Insertion**: Inserts initial data ('technology', 'e-commerce', 'gaming') into the `category` table.

4. **Data Update**: Updates the name of the category with `category_id` equal to 2 to 'online shop'.

5. **Commit Changes**: Commits the changes made to the database.

6. **Fetch and Print**: Fetches all categories from the `category` table and prints them.

7. **Database Connection Closure**: Closes the connection to the database.
