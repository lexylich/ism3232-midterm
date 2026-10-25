from business_rules import (
    calculate_job_total,
    calculate_print_cost,
    format_job_line,
    get_volume_discount,
    largest_job,
    needs_overnight_run,
    requires_proof,
    total_invoiced,
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


def test_job_total_at_exactly_40_dollars_has_no_fee():
    assert round(calculate_job_total(0.40, 100), 2) == 40.00


def test_job_total_just_under_40_dollars_adds_fee():
    assert round(calculate_job_total(0.39, 100), 2) == 54.00


def test_job_total_student_org_changes_the_answer():
    assert round(calculate_job_total(1.00, 200), 2) == 184.00
    assert round(calculate_job_total(1.00, 200, student_org=True), 2) == 174.00


def test_proof_not_required_at_exactly_300():
    assert requires_proof(300.00) is False


def test_proof_required_just_over_300():
    assert requires_proof(300.01) is True


def test_overnight_not_needed_at_exactly_500_copies():
    assert needs_overnight_run(500, 100.00) is False


def test_overnight_needed_at_501_copies():
    assert needs_overnight_run(501, 100.00) is True


def test_overnight_not_needed_at_exactly_400_dollars():
    assert needs_overnight_run(100, 400.00) is False


def test_overnight_needed_just_over_400_dollars():
    assert needs_overnight_run(100, 400.01) is True


def test_total_invoiced_adds_up_all_jobs():
    jobs = [
        {"title": "A", "copy_price": 1.00, "copies": 100, "student_org": False},
        {"title": "B", "copy_price": 1.00, "copies": 200, "student_org": False},
    ]
    assert round(total_invoiced(jobs), 2) == 100.00 + 184.00


def test_total_invoiced_empty_list_is_zero():
    assert total_invoiced([]) == 0.0


def test_largest_job_returns_title_of_biggest_total():
    jobs = [
        {"title": "Small", "copy_price": 1.00, "copies": 100, "student_org": False},
        {"title": "Big", "copy_price": 1.00, "copies": 500, "student_org": False},
    ]
    assert largest_job(jobs) == "Big"


def test_largest_job_tie_returns_first_in_list():
    jobs = [
        {"title": "First", "copy_price": 1.00, "copies": 100, "student_org": False},
        {"title": "Second", "copy_price": 1.00, "copies": 100, "student_org": False},
    ]
    assert largest_job(jobs) == "First"


def test_largest_job_empty_list_returns_empty_string():
    assert largest_job([]) == ""


def test_format_job_line_shows_no_for_false_values():
    assert (
        format_job_line("Flyers", 40.0, False, False)
        == "Flyers: $40.00 | proof: no | overnight run: no"
    )


def test_format_job_line_shows_yes_for_true_values():
    assert (
        format_job_line("Catalogs", 680.0, True, True)
        == "Catalogs: $680.00 | proof: yes | overnight run: yes"
    )
