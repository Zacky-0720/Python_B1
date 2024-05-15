import sys
args = sys.argv

station1 = args[1]
station2 = args[2]

distances = {'東京': 0,'品川': 6.78,'新横浜': 25.54,'名古屋': 342.02,'京都': 476.31,'新大阪': 515.35,}

list()
distance = station1 - station2
print(distance,end="")