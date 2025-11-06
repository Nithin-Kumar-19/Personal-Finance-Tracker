def generate_monthly_report(expenses):
    report = {}
    for expense in expenses:
        cat = expense['category']
        amount = float(expense['amount'])
        report[cat] = report.get(cat, 0) + amount

    print("Monthly Expense Report:")
    for category, total in report.items():
        print(f"{category}: ${total:.2f}")
