import csv


def record_expense(filename, date, category, amount, description):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])


def generate_report(filename):
    totals = {}
    with open(filename, "r", newline="") as file:  # 'file' is defined here
        reader = csv.reader(file)  # Now 'file' is an open file object
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            totals[category] = totals.get(category, 0) + amount
    print("Total Expenses by Category")
    print("--------------------------")
    for category, total in totals.items():
        print(f"{category:10} {total:10.2f}")
    print()



def get_total_expenses(filename):
    total = 0
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            amount = float(row[2])
            total += amount
    return total


def check_limit(filename, limit):
    total = get_total_expenses(filename)
    if total > limit:
        print(
            f"Warning: You have exceeded your limit of {limit:.2f}. Your total expenses are {total:.2f}."
        )
    else:
        print(
            f"You are within your limit of {limit:.2f}. Your total expenses are {total:.2f}"
        )


filename = "expenses.csv"
header = ["Date", "Category", "Amount", "Description"]
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
limit = 100000.00

answer = input("Do you want to record an expense? (y/n)")

while answer.lower() == "y":
    date = input("Enter the date of the expense (DD-MM-YYYY): ")
    category = input(
        "Enter the category of the expense (e.g Food, Transport, Rent, etc): "
    )
    amount = float(input("Enter the amount of the expense: "))
    description = input("Enter a brief description of the expense: ")
    record_expense(filename, date, category, amount, description)
    check_limit(filename, limit)
    answer = input("Do you want to record another expense? (y/n)")

if answer.lower() == "n":
    generate_report(filename)
    print("Thank you for using the expense tracker")
else:
    print ("Invalid input. Please enter either 'y' or 'n'.")