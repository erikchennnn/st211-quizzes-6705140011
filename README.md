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

### Pytest markers and test outcomes

- `pytest.ini` configures test discovery, concise tracebacks, strict marker checking, and the registered `smoke`, `slow`, and `regression` markers.
- `test_markers.py` demonstrates selecting smoke, slow, and regression test groups.
- `test_skips.py` demonstrates unconditional skipping and version-based conditional skipping.
- `test_xfail.py` demonstrates expected failures (`XFAIL`) and unexpected passes (`XPASS`).
- `test_conditional.py` skips its hosts-file test when `/etc/hosts` is unavailable.
- `test_strict.py` deliberately uses an unregistered marker to demonstrate the collection error produced by `--strict-markers`.

From the `assert_lab` folder, marker selections can be run in PowerShell with:

```powershell
pytest -m smoke -v
pytest -m "smoke or regression" -v
pytest -m "not slow" -v
```

To demonstrate strict marker validation, run:

```powershell
pytest test_strict.py
```

The error from this last command is intentional: `nonexistent_marker` is not registered in `pytest.ini`.

## Run the tests

From this folder, run:

```powershell
python -m pytest -v
```

Project-only files are tracked in Git; the virtual environment and pytest/Python cache folders are excluded through `.gitignore`.
