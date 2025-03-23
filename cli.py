# cli.py
from database import insert_expense, fetch_expenses, delete_expense

def add_expense():
    """Ask user for details and add an expense."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        insert_expense(amount, category, date)
    except ValueError:
        print("❌ Invalid input! Amount must be a number.")

def view_expenses():
    """Display all expenses in a readable format."""
    expenses = fetch_expenses()
    print("\n📌 Your Expenses:")
    print("=" * 40)
    print(f"{'ID':<5}{'Amount':<10}{'Category':<15}{'Date':<12}")
    print("=" * 40)
    for exp in expenses:
        print(f"{exp[0]:<5}{exp[1]:<10}{exp[2]:<15}{exp[3]:<12}")
    print("=" * 40)

def remove_expense():
    """Ask user for an ID to delete an expense."""
    try:
        expense_id = int(input("Enter the Expense ID to delete: "))
        delete_expense(expense_id)
    except ValueError:
        print("❌ Invalid ID! Must be a number.")
