import sys
args = sys.argv
name = args[1]

number = int(args[1])

if number % 2 == 0:
    print("偶数")
    
else:
    print("奇数")