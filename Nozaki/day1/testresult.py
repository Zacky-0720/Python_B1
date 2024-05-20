import sys
args = sys.argv

math = int(args[1])
language = int(args[2])
english = int(args[3])
 
    
if math >= 70 and language >= 70 and english >= 70:
        print("合格")

else:
    if math + language + english >= 220:
        if language >= 50 and math >= 50 and english >= 50:
            print("合格")
            
        else:
            print("不合格")
    
    else:
        print("不合格")
        

