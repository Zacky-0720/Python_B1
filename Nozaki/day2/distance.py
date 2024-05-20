import sys

# 引数から駅名を取得
station1 = sys.argv[1]
station2 = sys.argv[2]

# 駅間の距離を辞書で定義
distances = {'東京': 0, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

dis_from = distances[station1]
dis_to = distances[station2]

a = abs(dis_to - dis_from) 

print("{:.2f}".format(a), end="")
