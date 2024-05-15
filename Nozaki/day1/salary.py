import sys
args = sys.argv

Paid = int(args[1])

if Paid >= 1000000:
    tax_rate = 0.2

else:
    tax_rate = 0.1
    
tax_amount = int(round((min(Paid, 1000000)*0.1)+max(Paid-1000000,0)*0.2))

net_salary = Paid - tax_amount

print(net_salary)
print(tax_amount)
