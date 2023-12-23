def add(num1: int, num2: int):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2


def divide(num1: int, num2: int):
    return num1 / num2


class InsufficientFunds(Exception):
    pass


class InvlidAmount(Exception):
    pass


class BankAccount:
    def __init__(self, starting_balance=0) -> None:
        self.balance = starting_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return "Amount Deposited"
        else:
            raise InvlidAmount("Invalid Amount")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return "Done withdraw"

            else:
                raise InsufficientFunds("Insufficient funds")
        else:
            raise InvlidAmount("Invalid Amount")

    def collect_interest(self):
        self.balance *= 1.1

        # return self.balance

    def check_balance(self):
        return self.balance
