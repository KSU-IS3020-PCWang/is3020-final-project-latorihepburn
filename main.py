# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import csv

def load_expenses():
    expenses = []
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except FileNotFoundError:
        print("expenses.csv not found.")
    return expenses

def save_expenses(expenses):
    with open("expenses.csv", "w", newline="") as f:
        fieldnames = ["item", "category", "amount"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

def add_expense(expenses):
    item = input("Item: ")
    category = input("Category: ")
    amount = float(input("Amount: "))
    expenses.append({"item": item, "category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense added.")

def total_spent(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]
    return total

def highest_expense(expenses):
    if not expenses:
        return None
    highest = expenses[0]
    for exp in expenses:
        if exp["amount"] > highest["amount"]:
            highest = exp
    return highest

def average_expense(expenses):
    if not expenses:
        return 0
    return total_spent(expenses) / len(expenses)

def print_summary(expenses):
    print("\n--- Expense Summary ---")
    print("Total spent:", total_spent(expenses))
    print("Average expense:", average_expense(expenses))
    high = highest_expense(expenses)
    if high:
        print("Highest expense:", high["item"], "-", high["amount"])
    print("------------------------\n")

def main():
    expenses = load_expenses()

    while True:
        print("1. Add expense")
        print("2. View summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            print_summary(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()