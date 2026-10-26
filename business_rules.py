"""Business rules for Brightline Print Shop."""

# Discount tiers
LOW_VOLUME_LIMIT = 200
HIGH_VOLUME_LIMIT = 1000
STANDARD_DISCOUNT = 0.08
HIGH_VOLUME_DISCOUNT = 0.15
NO_DISCOUNT = 0.0

# Student organization bonus
STUDENT_ORG_BONUS = 0.05

# Fees and thresholds
SETUP_FEE_LIMIT = 40
SETUP_FEE = 15
PROOF_LIMIT = 300
OVERNIGHT_COPIES_LIMIT = 500
OVERNIGHT_TOTAL_LIMIT = 400

def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Return the print cost before any discount."""
    return copy_price * copies


def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if copies >= HIGH_VOLUME_LIMIT:
        discount = HIGH_VOLUME_DISCOUNT
    elif copies >= LOW_VOLUME_LIMIT:
        discount = STANDARD_DISCOUNT
    else:
        return NO_DISCOUNT
    if student_org:
        discount += STUDENT_ORG_BONUS
    return discount


def calculate_job_total(
    copy_price: float, copies: int, student_org: bool = False
) -> float:
    """Return the job total: discounted cost plus setup fee when it applies."""
    cost = calculate_print_cost(copy_price, copies)
    discount = get_volume_discount(copies, student_org)
    discounted = cost * (1 - discount)
    if discounted < SETUP_FEE_LIMIT:
        discounted += SETUP_FEE
    return discounted


def requires_proof(total: float) -> bool:
    """Return True when the job total requires a printed proof."""
    return total > PROOF_LIMIT


def needs_overnight_run(copies: int, total: float) -> bool:
    """Return True when the job needs an overnight press run."""
    return copies > OVERNIGHT_COPIES_LIMIT or total > OVERNIGHT_TOTAL_LIMIT


def total_invoiced(jobs: list) -> float:
    """Return the sum of the job totals for every job in the list."""
    total = 0.0
    for job in jobs:
        total += calculate_job_total(
            job["copy_price"], job["copies"], job["student_org"]
        )
    return total


def largest_job(jobs: list) -> str:
    """Return the title of the job with the largest job total."""
    largest_title = ""
    largest_total = 0.0
    for job in jobs:
        job_total = calculate_job_total(
            job["copy_price"], job["copies"], job["student_org"]
        )
        if largest_title == "" or job_total > largest_total:
            largest_title = job["title"]
            largest_total = job_total
    return largest_title


def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:
    """Return one report line for a job."""
    proof_text = "yes" if proof else "no"
    overnight_text = "yes" if overnight_run else "no"
    return (
        f"{title}: ${total:.2f} | proof: {proof_text} | overnight run: {overnight_text}"
    )
