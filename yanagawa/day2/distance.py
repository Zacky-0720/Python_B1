import sys

args = sys.argv

station_from = args[1]
station_to = args[2]

dic = {
    "東京": 0.00,
    "品川": 6.78,
    "新横浜": 25.54,
    "名古屋": 342.02,
    "京都": 476.31,
    "新大阪": 515.35,
}

distance = abs(dic[station_to] - dic[station_from])

print(round(distance, 2), end="")
