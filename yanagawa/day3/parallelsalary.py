import sys
import func_salary

args = sys.argv

salaries = map(int, args[1:])

for salary in salaries:
    pay_amount, tax_amount_sum = func_salary.calcsalary(salary)
    print(f"給与:{salary}、支給額:{pay_amount}、税額:{tax_amount_sum}")
