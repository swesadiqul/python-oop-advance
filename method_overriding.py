class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def get_balance(self):
        # Calculate the balance including interest
        return self.balance + (self.balance * self.interest_rate / 100)

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def get_balance(self):
        # Account for overdraft limit
        if self.balance < 0:
            return self.balance + self.overdraft_limit
        else:
            return self.balance


savings_acc = SavingsAccount("12345", 1000, 3.5)
checking_acc = CheckingAccount("67890", -200, 500)

print("Savings Account Balance:", savings_acc.get_balance())    # Output: Savings Account Balance: 1035.0
print("Checking Account Balance:", checking_acc.get_balance())  # Output: Checking Account Balance: 300
