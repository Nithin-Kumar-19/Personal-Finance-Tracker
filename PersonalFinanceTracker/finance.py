import csv
import os

expenses = []

def add_expense(amount, category, description):
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)

def save_to_csv(filename):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "category", "description"])
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense)
    except IOError as e:
        print(f"Error writing to {filename}: {e}")

def load_from_csv(filename):
    global expenses
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = [row for row in reader]
    except FileNotFoundError:
        print(f"{filename} not found.")
    except IOError as e:
        print(f"Error reading {filename}: {e}")
