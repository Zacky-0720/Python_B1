import sys

args = sys.argv

animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animal_list.insert(int(args[1]), args[2])
animal_list.pop()
new_animal_list = sorted(animal_list)

print(new_animal_list, end="")
