#奇数か偶数の判定
import sys
args=sys.argv
if(int(args[1])%2==0):
    print("偶数",end="") #偶数の場合
else:
    print("奇数",end="") #奇数の場合