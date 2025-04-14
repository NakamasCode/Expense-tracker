import sqlite3, json, hashlib
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
  
def get_all_expenses():
    """Fetch all expenses from database"""
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = cursor.fetchall()
    conn.close()
    return expenses
 
def get_expenses_by_category(category):
    """Fetch expenses filtered by category."""
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE category = ? ORDER BY date DESC", (category,))
    expenses = cursor.fetchall()
    conn.close()
    return expenses
    
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
   
def get_expenses_by_date(date):
    """Fetch expenses for a specific date."""
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date = ? ORDER BY date DESC", (date,))
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def get_expenses_sorted(by="amount", order="desc"):
    """Fetch expenses sorted by amount or date."""
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    
    if by not in ["amount", "date"]:
        print("Invalid sort field! Defaulting to amount.")
        by = "amount"
    
    order = "DESC" if order == "desc" else "ASC"
    query = f"SELECT * FROM expenses ORDER BY {by} {order}"
    
    cursor.execute(query)
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def update_expense(expense_id, new_amount=None, new_category=None, new_date=None):
    """Updates an expense and regenerates its hash for security."""
    
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    # Fetch the current expense details
    cursor.execute("SELECT amount, category, date FROM expenses WHERE id = ?", (expense_id,))
    row = cursor.fetchone()

    if not row:
        print("⚠️ Expense not found.")
        return False

    current_amount, current_category, current_date = row

    # Use the new values if provided, otherwise keep the old ones
    updated_amount = new_amount if new_amount is not None else current_amount
    updated_category = new_category if new_category is not None else current_category
    updated_date = new_date if new_date is not None else current_date

    # Generate new hash (since data is changing)
    data_string = f"{updated_amount}{updated_category}{updated_date}"
    new_hash = hashlib.sha256(data_string.encode()).hexdigest()

    # Update the record
    cursor.execute("""
        UPDATE expenses 
        SET amount = ?, category = ?, date = ?, hash = ?
        WHERE id = ?
    """, (updated_amount, updated_category, updated_date, new_hash, expense_id))

    conn.commit()
    conn.close()

    print("✅ Expense updated successfully!")
    return True

def delete_expense(expense_id):
    """Delete an expense by ID."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    print("🗑️ Expense deleted successfully!")
    
    
def export_to_json(filename="expenses.json"):
    """Exports all expenses from the database to a JSON file."""
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    if not expenses:
        print("⚠️ No expenses found to export.")
        return

    # Get column names for JSON keys
    column_names = [desc[0] for desc in cursor.description]

    # Convert to list of dictionaries
    expenses_list = [dict(zip(column_names, row)) for row in expenses]

    # Write to JSON file
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(expenses_list, json_file, indent=4)

    conn.close()
    print(f"✅ Expenses exported successfully to {filename}!")