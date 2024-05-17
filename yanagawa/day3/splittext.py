import sys

args = sys.argv

text = args[1]
num = int(args[2])

splitted_text = text.split(" ")

print(splitted_text[num - 1], end="")
