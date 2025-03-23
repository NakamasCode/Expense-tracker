import sqlite3
from utils import generate_hash

DB_NAME = "expenses.db"

def create_table():
   """Create the expenses table if it doesn't exist."""
   conn = sqlite3.connect(DB_NAME)
   cursor = conn.cursor()
   cursor.execute("""
   CREATE TABLE IF NOT EXISTS expenses(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      amount REAL,
      category TEXT,
      date TEXT,
      hash TEXT
   )
   """)
   
def insert_expense(amount, category, date):
   """Insert a new expense into the database"""
   conn = sqlite3.connect(DB_NAME)
   cursor = conn.cursor()
   
    # Generate a hash for data integrity
   expense_hash = generate_hash(amount, category, date)

   cursor.execute("INSERT INTO expenses (amount, category, date, hash) VALUES (?, ?, ?, ?)",
                   (amount, category, date, expense_hash))
   conn.commit()
   conn.close()
   print("✅ Expense added successfully!")
   
def fetch_expenses():
    """Retrieve all expenses from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def delete_expense(expense_id):
    """Delete an expense by ID."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    print("🗑️ Expense deleted successfully!")