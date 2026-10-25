"""Business rules for Brightline Print Shop."""

# Discount tiers
LOW_VOLUME_LIMIT = 200
HIGH_VOLUME_LIMIT = 1000
STANDARD_DISCOUNT = 0.08
HIGH_VOLUME_DISCOUNT = 0.15
NO_DISCOUNT = 0.0

# Student organization bonus
STUDENT_ORG_BONUS = 0.05


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
