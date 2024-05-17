import sys,datetime
args=sys.argv
date=datetime.date(int(args[1][:4]),int(args[1][4:6]),int(args[1][6:]))
adult_count=int(args[2])
child_count=int(args[3])
is_end_of_week=False
if date.strftime('%A') in ('Saturday','Sunday'):
    total=adult_count*2400+child_count*1500
else:
    total=adult_count*2000+child_count*1200
print(total,end="")