def calcsalary(payment):
    tax=0
    if payment>1000000:
        over_million=payment-1000000
        tax+=over_million*0.2
        tax+=1000000*0.1
        salary=payment-tax
    else:
        tax=payment*0.1
        salary=payment-tax
    return salary,tax