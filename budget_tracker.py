import csv
import os

DATA_FILE = 'budget_data.csv'

def load_data():
    """Load budget data from CSV."""
    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
    return data

def save_data(data):
    """Save budget data to CSV."""
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def add_transaction(description, amount, type_):
    """Add income or expense."""
    data = load_data()
    data.append([description, amount, type_])
    save_data(data)
    print(f"Added {type_}: {description} - ${amount}")

def view_balance():
    """Calculate and display balance."""
    data = load_data()
    income = sum(float(row[1]) for row in data if row[2] == 'income')
    expenses = sum(float(row[1]) for row in data if row[2] == 'expense')
    balance = income - expenses
    print(f"Total Income: ${income}")
    print(f"Total Expenses: ${expenses}")
    print(f"Balance: ${balance}")

def main():
    """Main function."""
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Description: ")
            amt = float(input("Amount: "))
            add_transaction(desc, amt, 'income')
        elif choice == "2":
            desc = input("Description: ")
            amt = float(input("Amount: "))
            add_transaction(desc, amt, 'expense')
        elif choice == "3":
            view_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()