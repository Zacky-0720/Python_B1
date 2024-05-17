import sys
args=sys.argv
text=args[1]
index=int(args[2])
text_array=text.split(' ')
print(text_array[index-1],end="")
