import sys

args = sys.argv

my_tuple = ("China", "India", "U.S.A", "Indonesia", "Pakistan",
            "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(my_tuple[int(args[1])-1], end="")