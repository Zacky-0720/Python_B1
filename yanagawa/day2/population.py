import sys

args = sys.argv

target_rank = int(args[1])

world_population_ranking = (
    "China",
    "India",
    "U.S.A",
    "Indonesia",
    "Pakistan",
    "Brazil",
    "Nigeria",
    "Bangladesh",
    "Russia",
    "Mexico",
)

print(world_population_ranking[target_rank - 1], end="")
