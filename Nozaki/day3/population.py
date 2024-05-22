# 第1引数の取得
import sys
# 第2引数の取得
a = int(sys.argv[1])

# 国名のリストを定義
population = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

# 配列0を考慮
b = a - 1

# リストから国名を出力する
print(population[b])