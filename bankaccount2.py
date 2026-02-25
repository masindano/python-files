'''
Masindano Masila
BSCIT-05-0133/2024
'''
"""
Interactive BankAccount Program with Validation
----------------------------------------------
This program:
- Accepts user input
- Prevents negative deposits
- Prevents negative withdrawals
- Prevents withdrawing more than available balance
- Provides a simple menu system
"""


class BankAccount:

    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        """
        Constructor method initializes account details.
        """
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits money into the account.
        Prevents negative or zero deposits.
        """
        if amount <= 0:
            return "Deposit amount must be greater than zero."

        self.balance += amount
        return f"{amount} deposited successfully."

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        Prevents negative withdrawal and overdrawing.
        """
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."

        if amount > self.balance:
            return "Insufficient balance."

        self.balance -= amount
        return f"{amount} withdrawn successfully."

    def check_balance(self):
        """
        Displays current balance.
        """
        print("Current Balance:", self.balance)

    def customer_details(self):
        """
        Displays all customer details.
        """
        print("\n--- Customer Details ---")
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)
        print("-------------------------")


# ==========================
# MAIN PROGRAM (INTERACTIVE)
# ==========================

# Get account details from user
acc_number = input("Enter Account Number: ")
name = input("Enter Customer Name: ")
date = input("Enter Date of Opening (YYYY-MM-DD): ")
initial_balance = float(input("Enter Initial Balance: "))

# Create BankAccount object
account = BankAccount(acc_number, name, date, initial_balance)

# Menu loop
while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Customer Details")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        print(account.deposit(amount))

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        print(account.withdraw(amount))

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.customer_details()

    elif choice == "5":
        print("Thank you for using the Bank System.")
        break

    else:
        print("Invalid choice. Please try again.")
