# Automated Software Testing (AST)

This repository contains introductory Python exercises and pytest tests completed in class.

## Code

- `bank.py` implements a `BankAccount` with deposit and withdrawal operations.
- `grades.py` converts a score from 0–100 to a letter grade and rejects invalid scores.

## Tests

- `test_bank.py` verifies that a deposit returns the expected new balance.
- `test_independent.py` uses a fresh `BankAccount` in each test, so its tests do not share state.
- `test_dependent.py` demonstrates dependent tests using one shared account.
- `test_grades.py` tests grade boundaries (80/79 and 60/59), valid limits (0 and 100), and an invalid score.

## Run the tests

From this folder, run:

```powershell
python -m pytest -v
```

Project-only files are tracked in Git; the virtual environment and pytest/Python cache folders are excluded through `.gitignore`.
