import sys
args=sys.argv
#辞書型の登録
km={'東京':0.00,'品川':6.78,'新横浜':25.54,'名古屋':342.02,'京都':476.31,'新大阪':515.35}
#距離の計算
distance=abs(km[args[1]]-km[args[2]])
#小数点の調整
Abs_distance=round(distance,2)
#結果の出力
print(Abs_distance,end="")