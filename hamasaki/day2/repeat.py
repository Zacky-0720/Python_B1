import sys

args = sys.argv
sum = 0

while sum < 100:
    sum += int(args[1])

if sum == 100:
    print("Just 100!", end="")
elif sum > 100:
    print("Over!", end="")

