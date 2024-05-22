import sys
args=sys.argv

with open("./koga/day5/sheep.txt",mode="w",encoding="utf-8") as tf:
    for i in range(1,int(args[1])+1):
        tf.write("ひつじが"+str(i)+"匹\n")
        i +=1