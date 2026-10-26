# Automated Software Testing (AST)

Python exercises and pytest tests completed in class, organized by lab topic.

## Test case lab (`testcase_lab`)

This folder covers positive, negative, and boundary testing, checking exceptions, and keeping tests independent.

| File | Purpose |
|---|---|
| `bank.py` | Bank account with deposit and withdrawal operations. |
| `grades.py` | Converts scores to letter grades and rejects scores outside 0-100. |
| `validators.py` | Validates email addresses and ages. |
| `test_bank.py` | Checks the balance after a deposit. |
| `test_grades.py` | Tests grade boundaries, valid limits, and an invalid score. |
| `test_positive.py` | Checks valid email addresses and ages. |
| `test_negative.py` | Checks exceptions for invalid emails and ages. |
| `test_independent.py` | Gives each test a fresh bank account. |
| `test_dependent.py` | Demonstrates tests that depend on a shared account's state. |

From the repository root:

```powershell
cd testcase_lab
python -m pytest -v
```

## Assertion lab (`assert_lab`)

This folder covers collection and floating-point assertions, shopping cart tests, test markers, skipping, and expected failures.

| File | Purpose |
|---|---|
| `shopping.py` | Shopping cart with methods to add items, count them, and calculate the total. |
| `test_shopping.py` | Checks an empty cart and its item count after adding an item. |
| `test_collections.py` | Tests lists, dictionaries, and set operations. |
| `test_floats.py` | Demonstrates floating-point precision and `pytest.approx`. |
| `test_markers.py` | Demonstrates smoke, slow, and regression labels on sample tests. |
| `test_skips.py` | Demonstrates unconditional and Python-version-based skips. |
| `test_conditional.py` | Skips a file check when `/etc/hosts` is unavailable. |
| `test_xfail.py` | Demonstrates expected failures and unexpected passes. |
| `test_strict.py` | Demonstrates an unregistered marker error with strict checking. |
| `pytest.ini` | Configures test discovery, output options, and registered markers. |

From the repository root, run the tests while excluding the intentional marker error:

```powershell
cd assert_lab
python -m pytest --ignore=test_strict.py -v
```

From inside `assert_lab`, select a test group or demonstrate the strict-marker error:

```powershell
python -m pytest --ignore=test_strict.py -m smoke
python -m pytest --ignore=test_strict.py -m "smoke or regression"
python -m pytest --ignore=test_strict.py -m "not slow"
python -m pytest test_strict.py
```

The last command intentionally produces a collection error because its marker is not registered.

## Parametrization lab (`param_lab`)

This folder covers running one test with multiple inputs, combining parameters, naming cases, parameterized fixtures, and loading test data from JSON and CSV files.

### Parameterized tests

| File | Purpose |
|---|---|
| `mathutils.py` | Functions for even-number checking and factorial calculation. |
| `test_param.py` | Tests several even and odd numbers. |
| `test_factorial.py` | Tests factorials from 0 through 5. |
| `discount.py` | Calculates discounts and rejects percentages outside 0-100. |
| `test_discount.py` | Checks several discounts, including no discount and a full discount. |
| `test_multi.py` | Stacks decorators to generate six input combinations. |
| `test_default_ids.py` | Demonstrates automatically generated test IDs. |
| `test_param_ids.py` | Gives discount cases readable custom IDs. |
| `test_param_marks.py` | Adds IDs and an expected-failure marker to individual cases. |

### Parameterized fixtures and external data

| File | Purpose |
|---|---|
| `test_param_fixture.py` | Uses browser-name strings to demonstrate fixture parameters, setup, and teardown with `yield`. |
| `test_browsers.py` | Uses database-name strings as fixture parameters despite its filename. |
| `test_cases.json` | Stores input and expected-output pairs for uppercase conversion. |
| `test_data_driven.py` | Loads the JSON cases and tests uppercase conversion. |
| `logins.csv` | Stores valid and empty-field login scenarios. |
| `validate.py` | Checks that both username and password are nonempty. |
| `test_csv_driven.py` | Loads CSV cases, converts expected values to booleans, and tests the validation function. |

The fixture examples use sample names; they do not open browsers or connect to databases. The login example checks empty fields rather than authenticating users.

From the repository root:

```powershell
cd param_lab
python -m pytest -v
```

Run from inside `param_lab` because its data loaders use relative paths to the JSON and CSV files. The square example in `test_param_marks.py` intentionally includes an expected failure.

## Useful test commands

With Python and pytest installed, run these from the relevant lab folder:

```powershell
python -m pytest test_discount.py -v  # Run one file in param_lab
python -m pytest -v -s               # Show print output
python -m pytest --collect-only -q   # List collected test cases
```

Each folder's instructions above start at the repository root. Use `cd ..` to return there before switching labs.
