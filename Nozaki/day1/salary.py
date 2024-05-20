import sys

Paid = int(sys.argv[1])

if Paid > 1000000:
    tax_rate =  int(1000000 * 0.1) + int(Paid - 1000000) * 0.2
else:
    tax_rate = int(Paid * 0.1)

tax = round(tax_rate)

salary = Paid - tax

print(f"支給額:{salary}、税額:{tax}", end="")