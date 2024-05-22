import sys
args = sys.argv
sum=0

while(sum<100):
    sum+=int(args[1])
    
    if (sum==100):
        print("just 100!", end="")
    else:
        print(sum)

    if(sum>100):
        print("Over!", end="")