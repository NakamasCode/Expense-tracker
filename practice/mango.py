import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()

cursor.execute('''
      CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         user_type TEXT NOT NULL --'Personal' or 'business'
         )
''')


cursor.execute('''
               CREATE TABLE IF NOT EXISTS expenses (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  amount REAL NOT NULL,
                  description TEXT,
                  category_id INTEGER,
                  date TEXT,
                  FOREIGN KEY(user_id) REFERENCES users(id),
                  FOREIGN KEY(category_id) REFERENCES category(id)
                  )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        user_id INTEGER,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

# Step 3: Commit changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")

