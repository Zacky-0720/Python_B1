import sys

args = sys.argv

num01 = int(args[1])
num02 = int(args[2])
num03 = int(args[3])

nums = (num01, num02, num03)


# 関数を定義
def calcvalue(num):
    # あまりを算出
    mod = num % 2

    # あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")


for i in nums:
    calcvalue(i)
