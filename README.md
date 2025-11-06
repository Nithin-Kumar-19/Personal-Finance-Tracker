# Personal Finance Tracker

A simple command-line Personal Finance Tracker in Python that allows you to add expenses, categorize them, save/load your data in CSV format, and generate monthly reports. This project demonstrates file operations, error handling, and modular coding with basic debugging best practices.

## Features

- Add new expenses with amount, category, and description
- Categorize each financial entry
- Save expenses to a CSV file for persistent storage
- Load expenses from CSV to continue where you left off
- Generate and view easy-to-read monthly summaries by category
- Error handling for robust file operations
- Modules split into multiple Python files for clarity and organization

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/yourusername/personal-finance-tracker.git
cd personal-finance-tracker
```

No special dependencies are needed (only the Python standard library).

### Usage

1. Place the project files (`main.py`, `finance.py`, `report.py`) in the same directory.
2. Open a terminal and run:

    ```bash
    python main.py
    ```

3. Use the menu to add expenses, generate reports, and manage your data.

### Files and Structure

| File         | Purpose                                                               |
|--------------|-----------------------------------------------------------------------|
| main.py      | Main control script and interactive menu                              |
| finance.py   | Core functions for adding, saving, and loading expenses               |
| report.py    | Functions for generating and displaying monthly reports               |
| expenses.csv | Saved file containing your expense data (created automatically)       |

### Example

```
Personal Finance Tracker
1. Add Expense
2. Save Expenses
3. Load Expenses
4. Generate Report
5. Exit
Choose an option:
```

Expense records are stored as rows in `expenses.csv` and can be reloaded on future runs to continue managing your finances.
