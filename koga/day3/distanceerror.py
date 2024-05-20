import sys
args=sys.argv

#辞書型の登録
km={'東京':0.00,'品川':6.78,'新横浜':25.54,'名古屋':342.02,'京都':476.31,'新大阪':515.35}

try:
    #距離の計算(引き算して絶対値を求める)
    distance=abs(km[args[1]]-km[args[2]])
    #浮動小数点の調整 round(値,表示する小数点の桁数)
    Abs_distance= round(distance,2)
    print(Abs_distance,end="")
except:
    print("のぞみの停車駅を引数に設定してください",end="")

