from business_rules import (
    calculate_print_cost,
    get_volume_discount,
)


def test_print_cost_is_price_times_copies():
    assert round(calculate_print_cost(0.25, 100), 2) == 25.00


def test_no_discount_at_199_copies():
    assert get_volume_discount(199) == 0.0


def test_standard_discount_at_exactly_200_copies():
    assert get_volume_discount(200) == 0.08


def test_standard_discount_at_999_copies():
    assert get_volume_discount(999) == 0.08


def test_high_discount_at_exactly_1000_copies():
    assert get_volume_discount(1000) == 0.15


def test_student_org_bonus_applies_at_200_copies():
    assert round(get_volume_discount(200, student_org=True), 2) == 0.13


def test_student_org_bonus_applies_at_1000_copies():
    assert round(get_volume_discount(1000, student_org=True), 2) == 0.20


def test_student_org_gets_no_bonus_under_200_copies():
    assert get_volume_discount(199, student_org=True) == 0.0
