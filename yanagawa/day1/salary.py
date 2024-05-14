import sys

args = sys.argv

base_salary = int(args[1])
threshold = 1000000

salary = base_salary

extra_salary = 0
if salary > threshold:
    extra_salary = salary - threshold
    salary = threshold

salary_tax_amount = salary * 0.1
extra_tax_amount = extra_salary * 0.2

tax_amount_sum = salary_tax_amount + extra_tax_amount

pay_amount = base_salary - tax_amount_sum

print(f"支給額:{int(pay_amount)}、税額:{int(tax_amount_sum)}", end="")
