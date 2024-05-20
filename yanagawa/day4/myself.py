import introduce
import sys

args = sys.argv

name, age = args[1:]

me = introduce.Intro(name, int(age))

print(me.name_out())
print(me.age_out())
