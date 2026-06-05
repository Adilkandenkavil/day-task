from typing import List


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner: str = owner
        self.balance: float = balance
        self.history: List[str] = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient Balance")

        self.balance -= amount
        self.history.append(f"Withdrawn ₹{amount}")

    def get_balance(self) -> float:
        return self.balance

    def transaction_history(self) -> List[str]:
        return self.history

    def __str__(self) -> str:
        return f"Owner: {self.owner}, Balance: ₹{self.balance}"
class SavingsAccount(BankAccount):
    def __init__(
        self,
        owner: str,
        balance: float,
        interest_rate: float
    ) -> None:
        super().__init__(owner, balance)
        self.interest_rate: float = interest_rate

    def apply_interest(self) -> None:
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.history.append(f"Interest Added ₹{interest}")
class CurrentAccount(BankAccount):
    def __init__(
        self,
        owner: str,
        balance: float,
        overdraft_limit: float
    ) -> None:
        super().__init__(owner, balance)
        self.overdraft_limit: float = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if self.balance - amount < -self.overdraft_limit:
            raise InsufficientFundsError("Overdraft Limit Exceeded")

        self.balance -= amount
        self.history.append(f"Withdrawn ₹{amount}")
if __name__ == "__main__":
    account = SavingsAccount("Rahees", 1000, 5)

    account.deposit(500)
    account.withdraw(200)
    account.apply_interest()

    print(account)
    print(account.transaction_history())