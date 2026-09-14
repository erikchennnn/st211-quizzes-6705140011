# Automated Software Testing (AST)

This repository contains introductory Python exercises and pytest tests completed in class.

## Test case lab

The original `exercise1` folder was renamed to `testcase_lab`.

- `bank.py` implements a `BankAccount` with deposit and withdrawal operations.
- `grades.py` converts a score from 0-100 to a letter grade and rejects invalid scores.
- `validators.py` validates email addresses and ages.
- `test_bank.py` verifies that a deposit returns the expected new balance.
- `test_independent.py` uses a fresh `BankAccount` in each test, so its tests do not share state.
- `test_dependent.py` demonstrates dependent tests using one shared account.
- `test_grades.py` tests grade boundaries, valid limits, and an invalid score.
- `test_positive.py` tests valid email addresses and ages.
- `test_negative.py` checks that invalid email addresses and ages raise the expected exceptions.

## Assertion lab

The `assert_lab` folder demonstrates several types of pytest assertions.

- `test_collections.py` tests list equality and contents, dictionary equality, and set operations.
- `test_floats.py` tests floating-point values using `pytest.approx` and demonstrates floating-point precision behavior.
- `shopping.py` implements a simple shopping cart that can add items, count items, and calculate their total price.
- `test_shopping.py` tests that a new shopping cart is empty, starts with a zero total, and increases its item count when an item is added.

## Run the tests

From this folder, run:

```powershell
python -m pytest -v
```

Project-only files are tracked in Git; the virtual environment and pytest/Python cache folders are excluded through `.gitignore`.
