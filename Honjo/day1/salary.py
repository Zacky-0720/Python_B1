import sys
args=sys.argv
payment=int(args[1])
tax=0
if payment>1000000:
    over_million=payment-1000000
    tax+=over_million*0.2
    tax+=1000000+0.1
    salary=payment-tax
else:
    tax=payment*0.1
    salary=payment-tax

print("支給額:"+str(int(round(salary,0)))+"、税額:"+str(int(round(tax,0))),end="")