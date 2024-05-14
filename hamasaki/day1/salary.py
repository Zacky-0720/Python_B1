import sys

args = sys.argv

payroll_amount = int(args[1])

if payroll_amount >= 1000000:
    tax_amount = (payroll_amount -1000000)*0.2 + 1000000*0.1
    
elif payroll_amount < 1000000:
    tax_amount = payroll_amount*0.1

# 小数第一位で四捨五入
rounded_tax_amount = round(tax_amount, 1)

rounded_tax_amount_int = int(rounded_tax_amount)

pay_amount = payroll_amount - rounded_tax_amount_int

print("支給額:" + str(pay_amount) + "、税額:" + str(rounded_tax_amount_int), end="")