import sys
args=sys.argv

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
animals.insert(int(args[1]),args[2])
del animals[5]
animals.sort()
print(animals, end="")