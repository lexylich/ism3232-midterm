# ISM3232 Midterm: Brightline Print Shop

- **Name:** Lexy Lichtenstein
- **Version:** Gamma
- **Date:** October 25, 2026

## What This Program Does

This program figures out the price of print jobs for Brightline Print Shop. It applies the discounts and fees, then checks which jobs need a proof or an overnight press run. It prints a report that the owner can read.

## Business Rules

- The print cost is the price per copy times the number of copies.
- Jobs under 200 copies get no discount. 200 to 999 copies get 8%. 1,000 or more get 15%.
- Student organizations get 5 extra points of discount, but only on jobs of 200 copies or more.
- A $15 setup fee is added when the discounted cost is under $40.
- A job total over $300 needs a printed proof.
- A job needs an overnight run if it has more than 500 copies or its total is over $400.

## How to Run

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

```
ruff format .
ruff check .
pytest -v
```

I wrote 24 tests.

## Files in This Repository

- `business_rules.py`: the eight functions that hold the business rules.
- `main.py`: the job list and the code that prints the report.
- `commands.md`: the terminal record of how I built and checked the project.
- `README.md`: this file.
- `requirements.txt`: the packages the project needs (pytest and ruff).
- `.gitignore`: keeps `.venv/` and `__pycache__/` out of the repository.
- `tests/__init__.py`: an empty file that makes `tests` a package.
- `tests/test_business_rules.py`: my pytest tests for the functions.

## AI Use Statement

I used no ai for this exam. I ran each command myself, and the terminal outputs from my own computer.