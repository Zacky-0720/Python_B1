import sys
args=sys.argv

animal_list=["giraffe","tiger","zebra","elephant","lion"]
animal_list.insert(int(args[1]),args[2])
del animal_list[5]
animal_list.sort()
print(animal_list,end="")