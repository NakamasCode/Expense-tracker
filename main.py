import cli

def main():
    while True:
        print("\n📌 EXPENSE TRACKER MENU")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Update Expense")
        print("4️⃣ Delete Expense")
        print("5️⃣ Export Expenses to JSON")
        print("6️⃣ Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            cli.add_expense()
        elif choice == "2":
            cli.view_expenses()
        elif choice == "3":
            cli.modify_expense()
        elif choice == "4":
            cli.remove_expense()
        elif choice == "5":
            cli.export_json()
        elif choice == "6":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
