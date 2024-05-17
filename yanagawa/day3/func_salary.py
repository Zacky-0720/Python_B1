def calcsalary(input_salary):
    threshold = 1000000

    base_salary = min(input_salary, threshold)
    extra_salary = max(0, input_salary - threshold)

    salary_tax_amount = round(base_salary * 0.1)
    extra_tax_amount = round(extra_salary * 0.2)

    tax_amount_sum = salary_tax_amount + extra_tax_amount

    pay_amount = input_salary - tax_amount_sum

    return pay_amount, tax_amount_sum
