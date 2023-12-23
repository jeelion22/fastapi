import pytest
from calculations import (
    add,
    subtract,
    multiply,
    divide,
    BankAccount,
    InsufficientFunds,
    InvlidAmount,
)


@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(1000)


@pytest.mark.parametrize(
    "num1, num2, expected", [(1, 2, 3), (8, 2, 10), (-10, -10, -20), (0, 0, 0)]
)
def test_add(num1, num2, expected):
    # print("testing add function")
    assert add(num1, num2) == expected


def test_subtract():
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(4, 2) == 2


def test_bank_set_initial(bank_account):
    assert bank_account.balance == 1000


def test_bank_default_amount(zero_bank_account):
    # bank_account = BankAccount()

    # assert bank_account.balance == 0
    assert zero_bank_account.balance == 0


@pytest.mark.parametrize(
    "amount, expected",
    [(0, "Invalid Amount"), (1050, "Insufficient funds")],
)
def test_withdraw(bank_account, amount, expected):
    # bank_account = BankAccount(1000)
    # bank_account.withdraw(500)

    # assert bank_account.balance == 500

    with pytest.raises(Exception):
        assert bank_account.withdraw(amount) == expected


@pytest.mark.parametrize(
    "amount, expected",
    [(250, "Done withdraw"), (320, "Done withdraw")],
)
def test_withdraw_without_exception(bank_account, amount, expected):
    # bank_account = BankAccount(1000)
    # bank_account.withdraw(500)

    # assert bank_account.balance == 500

    # with pytest.raises(Exception):
    assert bank_account.withdraw(amount) == expected


@pytest.mark.parametrize(
    "amount, expected", [(0, "Invalid Amount"), (-150, "Invalid Amount")]
)
def test_deposit(bank_account, amount, expected):
    # bank_account = BankAccount(1000)
    # bank_account.deposit(amount)

    # assert bank_account.balance == 1500
    with pytest.raises(Exception):
        assert bank_account.deposit(amount) == expected


@pytest.mark.parametrize(
    "amount, expected", [(1000, "Amount Deposited"), (12000, "Amount Deposited")]
)
def test_deposit_without_exception(bank_account, amount, expected):
    # bank_account = BankAccount(1000)
    # bank_account.deposit(amount)

    # assert bank_account.balance == 1500
    # with pytest.raises(Exception):
    assert bank_account.deposit(amount) == expected


def test_collect_intereset(bank_account):
    # bank_account = BankAccount(1000)
    bank_account.collect_interest()

    assert bank_account.balance == 1100.0


def test_check_balance(bank_account):
    # bank_account = BankAccount(1000)
    # bank_account_balance = bank_account.check_balance()

    assert round(bank_account.check_balance(), 6) == 1000
