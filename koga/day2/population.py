import sys
args=sys.argv

#タプルの追加(一番目→１位)
country=("China","India","U.S.A","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico")
#第一引数の順位に該当した国名を出力する
print(country[int(args[1])-1],end="")