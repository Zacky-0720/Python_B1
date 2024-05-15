import sys

args = sys.argv

target_index = int(args[1])
insertion_animal = args[2]

animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animal_list.insert(target_index, insertion_animal)
del animal_list[len(animal_list) - 1]
animal_list.sort()

print(animal_list, end="")
