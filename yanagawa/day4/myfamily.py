import sys
from introfamily import IntroFarm

args = sys.argv

name, age, cat_name = args[1:]


intro = IntroFarm(name, int(age), cat_name)

print(intro.name_out())
print(intro.age_out())
print(intro.cat_out())
