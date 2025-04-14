# cli.py
import database
import utils

def add_expense():
    """Ask user for details and add an expense."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        database.insert_expense(amount, category, date)
    except ValueError:
        print("❌ Invalid input! Amount must be a number.")

def view_expenses():
    """Display all expenses with filtering and sorting options."""
    print("\n1. View All Expenses")
    print("2. Filter by Category")
    print("3. Filter by Date")
    print("4. Sort by Amount")
    print("5. Sort by Date")
    choice = input("Choose an option: ")

    if choice == "1":
        expenses = database.get_all_expenses()
    elif choice == "2":
        category = input("Enter category: ")
        expenses = database.get_expenses_by_category(category)
    elif choice == "3":
        date = input("Enter date (YYYY-MM-DD): ")
        expenses = database.get_expenses_by_date(date)
    elif choice == "4":
        expenses = database.get_expenses_sorted(by="amount", order="desc")
    elif choice == "5":
        expenses = database.get_expenses_sorted(by="date", order="desc")
    else:
        print("Invalid choice!")
        return

    print("\n=== Expenses ===")
    for exp in expenses:
        print(exp)

def modify_expense():
    """Modify an existing expense."""
    expense_id = input("Enter Expense ID to update: ")

    new_amount = input("Enter new amount (or press enter to skip): ")
    new_amount = float(new_amount) if new_amount else None

    new_category = input("Enter new category (or press enter to skip): ")
    new_date = input("Enter new date (YYYY-MM-DD) (or press enter to skip): ")

    # Generate new hash
    new_hash = utils.generate_hash(expense_id, new_amount, new_category, new_date)

    success = database.update_expense(expense_id, new_amount, new_category, new_date, new_hash)
    if success:
        print("Expense updated successfully!")


def remove_expense():
    """Ask user for an ID to delete an expense."""
    try:
        expense_id = int(input("Enter the Expense ID to delete: "))
        database.delete_expense(expense_id)
    except ValueError:
        print("❌ Invalid ID! Must be a number.")
