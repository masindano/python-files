"""
===Author details===
Masindano Masila
BSCIT-05-0133/2024
"""
"""
BankAccount Class Program
-------------------------
This program defines a BankAccount class with the following:

Attributes:
- account_number
- customer_name
- date_of_opening
- balance

Methods:
- deposit()         -> Adds money to the account
- withdraw()        -> Withdraws money if sufficient balance exists
- check_balance()   -> Displays the current balance
- customer_details()-> Displays all customer account details
"""


class BankAccount:
    """
    The BankAccount class represents a simple bank account.
    It stores account details and allows deposit and withdrawal operations.
    """

    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        """
        Constructor method.
        This method is automatically called when a new BankAccount object is created.

        Parameters:
        account_number (str): The account number of the customer.
        customer_name (str): The name of the customer.
        date_of_opening (str): The date the account was opened.
        balance (float/int): The initial balance (default is 0).
        """

        # Assigning the provided values to the object attributes
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Parameter:
        amount (float/int): The amount to deposit.

        Returns:
        The amount deposited.
        """

        # Increase the account balance by the deposit amount
        self.balance += amount

        # Return the deposited amount
        return amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient balance exists.

        Parameter:
        amount (float/int): The amount to withdraw.

        Returns:
        - "Insufficient balance" if funds are not enough.
        - The amount withdrawn if successful.
        """

        # Check if the current balance is less than the withdrawal amount
        if self.balance < amount:
            return "Insufficient balance"

        # If balance is sufficient, deduct the amount
        self.balance -= amount
        return amount

    def check_balance(self):
        """
        Displays the current account balance.
        """

        print("Current Balance:", self.balance)

    def customer_details(self):
        """
        Displays all customer account details.
        """

        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)


# ==========================
# Example Usage of the Class
# ==========================

# Creating a new BankAccount object
acc1 = BankAccount("2543457", "Masindano Masila", "2026-02-25", 10000)

# Depositing money
print("Deposited:", acc1.deposit(5000))

# Withdrawing money
print("Withdrawn:", acc1.withdraw(3000))

# Checking balance
acc1.check_balance()

# Displaying full customer details
acc1.customer_details()
