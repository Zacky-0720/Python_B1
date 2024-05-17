import sys
args=sys.argv
class CityNotFoundError(Exception):
    pass
try:
    start=args[1]
    end=args[2]
    distances={'東京':0.00,'品川':6.78,'新横浜':25.54,'名古屋':342.02,'京都':476.31,'新大阪':515.35}
    if start in distances and end in distances:
        print(round(abs(distances[end]-distances[start]),2),end="")
    else:
        raise CityNotFoundError('のぞみの停車駅を引数に設定してください')
except CityNotFoundError as e:
    print(e,end="")
    