class Transaction:
    def make_transaction(self, amount, transaction_type="deposit"):
        if transaction_type == "deposit":
            self.deposit(amount)
        elif transaction_type == "withdraw":
            self.withdraw(amount)
        elif transaction_type == "transfer":
            self.transfer(amount)
        else:
            print("Invalid transaction type")

    def deposit(self, amount):
        print(f"Depositing ${amount}")

    def withdraw(self, amount):
        print(f"Withdrawing ${amount}")

    def transfer(self, amount):
        print(f"Transferring ${amount}")


transaction = Transaction()
transaction.make_transaction(100)  # Deposit $100
transaction.make_transaction(50, "withdraw")  # Withdraw $50
transaction.make_transaction(200, "transfer")  # Transfer $200
transaction.make_transaction(300, "invalid")  # Invalid transaction type
