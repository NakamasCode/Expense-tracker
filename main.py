import sqlite3
import hashlib

# connect to Sqlite (creates the file if it doesnt exist)
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# create expense table
cursor.execute("""
   CREATE TABLE IF NOT EXISTS expenses (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      amount REAL NOT NULL,
      category TEXT NOT NULL,
      date TEXT NOT NULL,
      hash TEXT NOT NULL
   )
""")

#commit and close connection
conn.commit()
conn.close()

def generate_hash(amount, category, date):
   # Generate a unique sha-256 hash for an expense.
   hash_input = f"{amount}{category}{date}".encode()
   return hashlib.sha256(hash_input).hexdigest()

def insert_expense(amount, category, date):
    """Insert a new expense into the database."""
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    
    # Generate a hash
    expense_hash = generate_hash(amount, category, date)

    cursor.execute("""
    INSERT INTO expenses (amount, category, date, hash)
    VALUES (?, ?, ?, ?)
    """, (amount, category, date, expense_hash))

    conn.commit()
    conn.close()

    print("✅ Expense added successfully!")

def fetch_expense():
   """Retrieve and display expenses from the database."""
   conn.sqlite3.connect('expenses.db')
   cursor = conn.cursor()
   
   cursor.execute("SELECT * FROM expenses")
   rows = cursor.fetchall()
   
   conn.close()
# Example usage (you can modify this for user input)
amount = float(input("Enter amount: "))
category = input("Enter category: ")
date = input("Enter date (YYYY-MM-DD): ")

insert_expense(amount, category, date)