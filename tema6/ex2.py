class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def calculate_interest(self):
        raise NotImplementedError("Subclasses should implement this method.")


class SavingsAccount(Account):
    def calculate_interest(self, rate=0.03):
        interest = self.balance * rate
        self.deposit(interest)
        print(f"Interest of ${interest} calculated and added to the account.")


class CheckingAccount(Account):
    def calculate_interest(self):
        print("Checking accounts do not earn interest.")


savings_account = SavingsAccount("SAV-001", 2000)
checking_account = CheckingAccount("CHK-101", 1000)

savings_account.deposit(1200)
checking_account.withdraw(500)

savings_account.calculate_interest()
checking_account.calculate_interest()
