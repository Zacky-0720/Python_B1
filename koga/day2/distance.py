import sys
args=sys.argv
#辞書型の登録
km={'東京':0.00,'品川':6.78,'新横浜':25.54,'名古屋':342.02,'京都':476.31,'新大阪':515.35}
#距離の計算(引き算して絶対値を求める)
distance=abs(km[args[1]]-km[args[2]])
#浮動小数点の調整 (数値を100倍して小数点部分(3桁以降に当たる部分)を消去して再び100で割る)
import math
Abs_distance= math.floor(distance * 100) / 100
#結果の出力
print(Abs_distance,end="")