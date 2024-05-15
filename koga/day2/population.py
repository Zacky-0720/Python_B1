import sys
args=sys.argv

country=("China","India","U.S.A","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico")
print(country[int(args[1])-1],end="")