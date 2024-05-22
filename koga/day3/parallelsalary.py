import sys
args=sys.argv

import func_salary 

for i in range(len(args)-1):
    V=func_salary.calcsalary(int(args[i+1]))
    salary=args[i+1]
    pay_salary=V[0]
    tax=V[1]
    print("給与："+str(salary)+"、"+"支給額："+str(pay_salary)+"、"+"税額："+str(tax))

