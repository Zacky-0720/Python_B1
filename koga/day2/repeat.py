#任意の値を、100を超えるまで足し続ける
import sys
args=sys.argv
#合計を示す変数を設置
sum=0

#100になるまでsumに任意の引数を足す。
while(sum<100):
    sum+=int(args[1])
#100を超えた後の処理
#ちょうど100の場合
if (sum==100):
      print("Just 100!",end="")
#100を超えた場合        
if(sum>100):
    print("Over!",end="")