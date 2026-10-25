from business_rules import (
    calculate_job_total,
    format_job_line,
    largest_job,
    needs_overnight_run,
    requires_proof,
    total_invoiced,
)

jobs = [
    {"title": "Flyers", "copy_price": 0.25, "copies": 100, "student_org": False},
    {"title": "Menus", "copy_price": 0.50, "copies": 150, "student_org": True},
    {"title": "Posters", "copy_price": 1.20, "copies": 250, "student_org": False},
    {"title": "Programs", "copy_price": 0.80, "copies": 500, "student_org": True},
    {"title": "Catalogs", "copy_price": 0.40, "copies": 2000, "student_org": False},
    {"title": "Banners", "copy_price": 3.00, "copies": 120, "student_org": False},
    {"title": "Tickets", "copy_price": 0.10, "copies": 501, "student_org": False},
    {"title": "Booklets", "copy_price": 1.75, "copies": 300, "student_org": True},
]

proof_count = 0
overnight_count = 0

print("Brightline Print Shop - Job Report")
for job in jobs:
    total = calculate_job_total(job["copy_price"], job["copies"], job["student_org"])
    proof = requires_proof(total)
    overnight = needs_overnight_run(job["copies"], total)
    if proof:
        proof_count += 1
    if overnight:
        overnight_count += 1
    print(format_job_line(job["title"], total, proof, overnight))

grand_total = total_invoiced(jobs)
average = grand_total / len(jobs)

print(f"Jobs: {len(jobs)}")
print(f"Total invoiced: ${grand_total:.2f}")
print(f"Average job total: ${average:.2f}")
print(f"Largest job total: {largest_job(jobs)}")
print(f"Proofs required: {proof_count}")
print(f"Overnight runs: {overnight_count}")
