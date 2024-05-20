import sys
args = sys.argv

def calcvalue(num):
    # あまりを算出
    mod = int(num) % 2
    
    # あまりの値から奇数偶数の判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

for i in args[1:]:
    calcvalue(i)