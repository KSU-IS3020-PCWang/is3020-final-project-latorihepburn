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
    """
    Load expenses from expenses.csv and return a list of dictionaries.
    Each dictionary contains: item, category, amount.
    """
    expenses = []
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert amount to float for calculations
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except FileNotFoundError:
        print("Error: expenses.csv not found. Starting with an empty list.")
    return expenses


def save_expenses(expenses):
    """
    Save the list of expenses back into expenses.csv.
    """
    with open("expenses.csv", "w", newline="") as f:
        fieldnames = ["item", "category", "amount"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)


def add_expense(expenses):
    """
    Prompt the user for expense details and add the new expense.
    """
    print("\n--- Add New Expense ---")
    item = input("Item name: ")
    category = input("Category: ")

    # Validate amount input
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Please enter a valid number for the amount.")

    expenses.append({"item": item, "category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense added successfully.\n")


def total_spent(expenses):
    """
    Return the total amount spent across all expenses.
    """
    return sum(exp["amount"] for exp in expenses)


def highest_expense(expenses):
    """
    Return the expense with the highest amount.
    If no expenses exist, return None.
    """
    if not expenses:
        return None
    return max(expenses, key=lambda x: x["amount"])


def average_expense(expenses):
    """
    Return the average expense amount.
    If no expenses exist, return 0.
    """
    if not expenses:
        return 0
    return total_spent(expenses) / len(expenses)


def print_summary(expenses):
    """
    Print a formatted summary of total, average, and highest expense.
    """
    print("\n--- Expense Summary ---")
    print(f"Total spent: ${total_spent(expenses):.2f}")
    print(f"Average expense: ${average_expense(expenses):.2f}")

    high = highest_expense(expenses)
    if high:
        print(f"Highest expense: {high['item']} - ${high['amount']:.2f}")
    else:
        print("No expenses recorded yet.")
    print("------------------------\n")


def main():
    """
    Main program loop: load expenses, show menu, and respond to user choices.
    """
    expenses = load_expenses()

    while True:
        print("Expense Tracker Menu")
        print("1. Add expense")
        print("2. View summary")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            print_summary(expenses)
        elif choice == "3":
            print("Goodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


# Run the program
main()

