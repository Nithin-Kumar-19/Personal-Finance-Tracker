import os
from finance import add_expense, save_to_csv, load_from_csv, expenses
from report import generate_monthly_report

def main():
    filename = 'expenses.csv'
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. Save Expenses")
        print("3. Load Expenses")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")
                add_expense(amount, category, description)
            except ValueError:
                print("Invalid input for amount.")
        elif choice == '2':
            save_to_csv(filename)
        elif choice == '3':
            load_from_csv(filename)
        elif choice == '4':
            generate_monthly_report(expenses)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
