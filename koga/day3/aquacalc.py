import sys
args=sys.argv

#曜日判定の関数
def weekly(date):
    #入力数値を日と月に分割(日は整数型、月は文字列)
    month=date[4:6]
    day=int(date[6:8])
    #各月のパターン別に日付を算出
    if(month=="01"):
        sum_date=day
    if(month=="02"):
        sum_date=31+day
    if(month=="03"):
        sum_date=59+day
    if(month=="04"):
        sum_date=90+day
    if(month=="05"):
        sum_date=120+day    
    if(month=="06"):
        sum_date=151+day
    if(month=="07"):
        sum_date=181+day
    if(month=="08"):
        sum_date=212+day
    if(month=="09"):
        sum_date=243+day
    if(month=="10"):
        sum_date=273+day
    if(month=="11"):
        sum_date=304+day
    if(month=="12"):
        sum_date=334+day
    #７で割った余りを利用して曜日区分を導出
    if(sum_date%7==1 or sum_date%7==2):
        return(True)
    else:
        return(False)

#第一引数に応じて曜日区分を出力(True=休日、False=平日)
V=weekly(args[1])

#曜日ごとの値段表(辞書型)
weekday={"大人":2000,"子供":1200}
holiday={"大人":2400,"子供":1500}

#日付によって異なる値段計算を実行
#休日の場合
if(V==True):
    Price=holiday["大人"]*int(args[2])+holiday["子供"]*int(args[3])
#平日の場合
if(V==False):
    Price=weekday["大人"]*int(args[2])+weekday["子供"]*int(args[3])

# 合計金額の出力
print(Price,end="")
    