class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        self.history.append(f"Deposited: {amount}")
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self.balance:
            raise InsufficientFundsError("Balance is too low")

        self.balance -= amount
        self.history.append(f"Withdrawn: {amount}")
        print(f"{amount} withdrawn successfully")

    def get_balance(self):
        return self.balance

    def transaction_history(self):
        return self.history

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.history.append(f"Interest added: {interest}")
        print(f"Interest of {interest} added successfully")


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if self.balance - amount < -self.overdraft_limit:
            raise InsufficientFundsError("Overdraft limit exceeded")

        self.balance -= amount
        self.history.append(f"Withdrawn: {amount}")
        print(f"{amount} withdrawn successfully")
print("===== Normal Bank Account =====")

account = BankAccount("Sahad", 1000)

print(account)

account.deposit(500)
account.withdraw(300)

print("Balance:", account.get_balance())
print("History:", account.transaction_history())

try:
    account.withdraw(2000)
except InsufficientFundsError as e:
    print("Error:", e)


print("\n      Savings Account      ")

savings = SavingsAccount("Ravi", 2000, 5)

print(savings)

savings.deposit(1000)
savings.apply_interest()

print("Balance:", savings.get_balance())
print("History:", savings.transaction_history())


print("\n      Current Account       ")

current = CurrentAccount("Anu", 1000, 500)

print(current)

current.withdraw(1200)

print("Balance:", current.get_balance())

try:
    current.withdraw(500)
except InsufficientFundsError as e:
    print("Error:", e)

print("History:", current.transaction_history())