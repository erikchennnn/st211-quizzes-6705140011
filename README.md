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

## Parametrization lab (12 October 2026)

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

Run all tests from today's lab from the repository root:

```powershell
python -m pytest param_lab -v
```

The expected result is **34 passed, 1 xfailed**. To inspect the generated test IDs without running the tests:

```powershell
python -m pytest param_lab --collect-only -q
```

## Run the tests

From this folder, run:

```powershell
python -m pytest -v
```

The full run includes the intentional strict-marker collection error described above. Use the lab-specific command to run only the parametrization exercises.

Project-only files are tracked in Git; the virtual environment and pytest/Python cache folders are excluded through `.gitignore`.
