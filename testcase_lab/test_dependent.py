from bank import BankAccount

shared_account = BankAccount(100)

def test_deposit_independent():
    shared_account.deposit(50)
    assert shared_account.balance == 150

def test_withdraw_independent():
    shared_account.withdraw(30)
    assert shared_account.balance == 120