import sys,func_salary
args=sys.argv
payments=args[1:]
for payment in payments:
    salary,tax=func_salary.calcsalary(int(payment))
    print("給与:"+payment+"、支給額:"+str(int(round(salary,0)))+"、税額:"+str(int(round(tax,0))))