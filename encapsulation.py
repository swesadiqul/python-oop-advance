# 1: ATM Machine

class ATM:
    def __init__(self):
        self.balance = 10000

    def withdraw(self, amount, pin):
        if pin == 1234:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrawal successful. Remaining balance: {self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Incorrect PIN."

atm = ATM()
print(atm.withdraw(2000, 1234))    # Output: "Withdrawal successful. Remaining balance: 8000"
print(atm.withdraw(5000, 9999))    # Output: "Incorrect PIN."
print(atm.withdraw(12000, 1234))   # Output: "Insufficient funds."











































# 2: Email System
# class Email:
#     def __init__(self):
#         self.__content = ""

#     def set_content(self, content, password):
#         if password == "secret":
#             self.__content = content
#         else:
#             return "Incorrect password."

#     def get_content(self, password):
#         if password == "secret":
#             return self.__content
#         else:
#             return "Incorrect password."

# email = Email()
# email.set_content("Hello, this is a secret email.", "secret")
# print(email.get_content("secret"))   # Output: "Hello, this is a secret email."
# print(email.get_content("wrongpass")) # Output: "Incorrect password."
