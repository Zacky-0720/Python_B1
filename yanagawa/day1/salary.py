import sys

args = sys.argv

input_salary = int(args[1])
threshold = 1000000

base_salary = min(input_salary, threshold)
extra_salary = max(0, input_salary - threshold)

salary_tax_amount = round(base_salary * 0.1)
extra_tax_amount = round(extra_salary * 0.2)

tax_amount_sum = salary_tax_amount + extra_tax_amount

pay_amount = input_salary - tax_amount_sum

print(f"支給額:{pay_amount}、税額:{tax_amount_sum}", end="")
