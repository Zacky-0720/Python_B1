import sys
args=sys.argv

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

Number = int(args[1])
divisor_list=[]

while(Number%i==0):
     Number=Number/i
else:
     