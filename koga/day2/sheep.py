import sys
args=sys.argv
#1から引数まで、ひつじを数える。(1から数えて1足す)
#for i in range(1,int(args[1])+1):
    #print("ひつじが"+str(i)+"匹")
    #i +=1
#1から引数まで、ひつじを数える。(0に1足してから数える。)
#for i in range(0,int(args[1])):
    #i +=1
    #print("ひつじが"+str(i)+"匹")
    
for i in range(int(args[1])):
    i +=1
    print("ひつじが"+str(i)+"匹")