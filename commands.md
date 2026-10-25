# Terminal Record: Brightline Print Shop

## 1. Building the project

```
mkdir ~/ism3232-midterm
cd ~/ism3232-midterm
git init
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
touch business_rules.py main.py commands.md README.md .gitignore
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
pip freeze > requirements.txt
git add .
git commit -m "Start midterm: add project skeleton"
git branch -M main
git remote add origin https://github.com/lexylich/ism3232-midterm.git
git push -u origin main
```

## 2. The virtual environment

```
which python3
```

```
/Users/lexylichtenstein/ism3232-midterm/.venv/bin/python3
```

The path goes through the `.venv` folder inside my project, which shows the virtual environment is active.


## 3. The project structure

```
tree -L 2
```

```
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The `__pycache__` folder is on my computer but not in my GitHub repository, because `.gitignore` tells git to skip it since Python regenerates it automatically.

## 4. Every function and test

```
rg 'def '
```

```
business_rules.py
14:def calculate_print_cost(copy_price: float, copies: int) -> float:
19:def get_volume_discount(copies: int, student_org: bool = False) -> float:
40:def calculate_job_total(
52:def requires_proof(total: float) -> bool:
57:def needs_overnight_run(copies: int, total: float) -> bool:
62:def total_invoiced(jobs: list) -> float:
72:def largest_job(jobs: list) -> str:
86:def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:

tests/test_business_rules.py
13:def test_print_cost_is_price_times_copies():
17:def test_no_discount_at_199_copies():
21:def test_standard_discount_at_exactly_200_copies():
25:def test_standard_discount_at_999_copies():
29:def test_high_discount_at_exactly_1000_copies():
33:def test_student_org_bonus_applies_at_200_copies():
37:def test_student_org_bonus_applies_at_1000_copies():
41:def test_student_org_gets_no_bonus_under_200_copies():
45:def test_job_total_at_exactly_40_dollars_has_no_fee():
49:def test_job_total_just_under_40_dollars_adds_fee():
53:def test_job_total_student_org_changes_the_answer():
58:def test_proof_not_required_at_exactly_300():
62:def test_proof_required_just_over_300():
66:def test_overnight_not_needed_at_exactly_500_copies():
70:def test_overnight_needed_at_501_copies():
74:def test_overnight_not_needed_at_exactly_400_dollars():
78:def test_overnight_needed_just_over_400_dollars():
82:def test_total_invoiced_adds_up_all_jobs():
90:def test_total_invoiced_empty_list_is_zero():
94:def test_largest_job_returns_title_of_biggest_total():
102:def test_largest_job_tie_returns_first_in_list():
110:def test_largest_job_empty_list_returns_empty_string():
114:def test_format_job_line_shows_no_for_false_values():
121:def test_format_job_line_shows_yes_for_true_values():
```

`business_rules.py` defines 8 functions, and `tests/test_business_rules.py` defines 24 tests.

## 5. Which files print

```
rg -l 'print'
```

```
commands.md
business_rules.py
main.py
tests/test_business_rules.py
```

`main.py` is the only Python file that calls `print()`. `business_rules.py` shows up in the list only because the word "print" appears in names like `calculate_print_cost`, not because it prints anything.

## 6. The commit history

```
git log --oneline
```

```
021a482 (HEAD -> main, origin/main) Add main.py with job report
eb26630 Add total, largest, and line format functions with tests
8a0b47a Add job total, proof, and overnight run functions with tests
085b74e Add print cost and volume discount functions with tests
2b969eb Start midterm: add project skeleton
```

There were 5 commits at that point.