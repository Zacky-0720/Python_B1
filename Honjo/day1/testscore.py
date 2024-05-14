import sys
args=sys.argv
math=int(args[1])
japanese=int(args[2])
english=int(args[3])
total=math+japanese+english
condition1=(math>=70 and japanese>=70 and english>=70) or total>=220
condition2=math>=50 and japanese>=50 and english>=50
if condition1 and condition2:
    print("合格",end="")
else:
    print("不合格",end="")