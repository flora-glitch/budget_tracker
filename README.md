# Personal Budget Tracker

A simple command-line application to track personal income and expenses, calculate balance, and save data to a CSV file.

## Features

- Add income transactions
- Add expense transactions
- View current balance (income - expenses)
- Data persistence using CSV file (`budget_data.csv`)

## Requirements

- Python 3.x
- Built-in `csv` module (no external dependencies)

## How to Run

1. Navigate to the project directory:
   ```
   cd BasicProjects/Python
   ```

2. Run the script:
   ```
   python budget_tracker.py
   ```

3. Follow the menu prompts:
   - Choose 1 to add income
   - Choose 2 to add expense
   - Choose 3 to view balance
   - Choose 4 to exit

## Usage Example

```
Budget Tracker Menu:
1. Add Income
2. Add Expense
3. View Balance
4. Exit
Choose an option: 1
Description: Salary
Amount: 3000
Task 'Salary' added.

Choose an option: 2
Description: Rent
Amount: 1000
Task 'Rent' added.

Choose an option: 3
Total Income: $3000.0
Total Expenses: $1000.0
Balance: $2000.0
```

## Data Storage

Transactions are saved to `budget_data.csv` in the same directory as the script. The file contains columns for description, amount, and type (income/expense).

## Notes

- Amounts are stored as floats.
- The application loads existing data on startup and saves changes automatically.
- No data validation for negative amounts or invalid inputs beyond basic error handling.
