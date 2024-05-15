import sys

args = sys.argv

input_num = int(args[1])
sum = 0

while sum < 100:
    sum += input_num

if sum == 100:
    print("Just 100!", end="")
else:
    print("Over!", end="")
