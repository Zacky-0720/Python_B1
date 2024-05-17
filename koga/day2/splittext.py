import sys
args=sys.argv

s=args[1]
split_text=s.split()
print(split_text[int(args[2])-1],end="")
