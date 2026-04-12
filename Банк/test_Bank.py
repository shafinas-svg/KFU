import pytest
from bank import BankAccount


def test_initial_balance():
    acc = BankAccount(100)
    assert acc.balance == 100


def test_deposit():
    acc = BankAccount(100)
    acc.deposit(50)
    assert acc.balance == 150


def test_withdraw_success():
    acc = BankAccount(100)
    acc.withdraw(40)
    assert acc.balance == 60


def test_withdraw_not_enough_money():
    acc = BankAccount(100)
    with pytest.raises(ValueError):
        acc.withdraw(200)


def test_transfer_success():
    acc1 = BankAccount(100)
    acc2 = BankAccount(50)

    acc1.transfer(acc2, 30)

    assert acc1.balance == 70
    assert acc2.balance == 80


def test_transfer_not_enough_money():
    acc1 = BankAccount(100)
    acc2 = BankAccount(50)

    with pytest.raises(ValueError):
        acc1.transfer(acc2, 200)