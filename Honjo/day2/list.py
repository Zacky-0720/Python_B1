import sys
args=sys.argv
index=int(args[1])
animal=args[2]
list=['giraffe','tiger','zebra','elephant','lion']
list.insert(index,animal)
list.pop()
list.sort()
print(list)