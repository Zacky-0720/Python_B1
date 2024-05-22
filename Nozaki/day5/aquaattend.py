# 第1引数の取得
import sys
import datetime
args = sys.argv

# 曜日の取得
# datestring = args[1]

# year = int(args[0:5])
# month = int(args[5:8])
# day = int(args[8:11])

year = int(args[1])
month = int(args[2])
day = int(args[3])
date = datetime.date(year, month, day)
week = date.weekday()

# 第3,4引数の取得
adult = int(args[4])
child = int(args[5])

# 条件式
if week > 4:
    print(2400*int(args[4]) + 1500*int(args[5]))
else:
    print(2000*int(args[4]) + 1200*int(args[5]))