import sys
args = sys.argv

s_distans = {'東京': 0, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

try:
    distans = round(abs(s_distans[args[1]] - s_distans[args[2]]), 2)
    print(distans)

except:
    print("のぞみの停車駅を引数に設定してください")
    