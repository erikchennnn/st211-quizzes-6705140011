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

## Parametrization lab (12 and 19 October 2026)

The `param_lab` folder practices running the same test with multiple inputs using `pytest.mark.parametrize`.

- `mathutils.py` implements even-number checking and factorial calculation.
- `test_param.py` checks five even numbers and five odd numbers.
- `test_factorial.py` checks factorials from 0 through 5.
- `discount.py` calculates percentage discounts and rejects percentages outside 0-100.
- `test_discount.py` checks five discount cases, including no discount and a full discount.
- `test_multi.py` stacks parametrization decorators to generate all six combinations of three `x` values and two `y` values.
- `test_default_ids.py` demonstrates pytest's generated IDs for dictionary inputs.
- `test_param_ids.py` uses `pytest.param(..., id=...)` to give discount cases readable names.
- `test_param_marks.py` adds IDs and an `xfail` marker to individual cases. The `known_bug` case deliberately expects `5 ** 2` to equal 20 to demonstrate an expected failure.

### Parameterized fixtures and external test data (19 October 2026)

- `test_param_fixture.py` supplies Chrome, Firefox, and Safari names through a parameterized fixture. Two tests run for each name, producing six cases and demonstrating setup and teardown with `yield`.
- `test_browsers.py` supplies SQLite, PostgreSQL, and MySQL names through a parameterized fixture, producing three cases. Despite the filename, this exercise uses database names.
- These fixture examples use strings to demonstrate parameterization; they do not launch real browsers or connect to databases.
- `test_cases.json` stores four input/expected-output pairs for uppercase conversion.
- `test_data_driven.py` loads the JSON data and generates a separate uppercase test for each pair.
- `logins.csv` stores four login-validation scenarios, including empty username and empty password cases.
- `validate.py` checks that both username and password are nonempty. It does not authenticate users or block particular usernames.
- `test_csv_driven.py` reads the CSV scenarios, converts the expected-result column to booleans, and checks each scenario independently.

### Run the parametrization lab

From the repository root, enter `param_lab` before running tests because the data loaders open JSON and CSV files relative to the current directory:

```powershell
Set-Location param_lab
python -m pytest -v
```

Verified on 19 October 2026: **51 passed, 1 xfailed**. The expected failure is the deliberate square example described above. To inspect the generated test IDs without running the tests, use the same directory:

```powershell
python -m pytest --collect-only -q
```

## Run the tests

With Python and pytest installed in your active environment, run each lab from its own directory. For example, from the repository root:

```powershell
Set-Location testcase_lab
python -m pytest -v
```

The assertion lab includes the intentional strict-marker collection error described above. The parametrization lab requires its own working directory for the external data files, so use its commands above rather than running every lab together from the repository root.

Project-only files are tracked in Git; the virtual environment and pytest/Python cache folders are excluded through `.gitignore`.
