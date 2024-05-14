import sys
args=sys.argv
args.pop(0)
sum=0
for number in args:
    sum+=int(number)
print(sum,end="")