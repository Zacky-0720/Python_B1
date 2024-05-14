import sys
args=sys.argv
#
score_math=int(args[1])
score_Japanese=int(args[2])
score_English=int(args[3])

if(((score_math>=70 and score_Japanese>=70 and score_math>=50) or (score_math+score_Japanese+score_English>=220)) and ((score_math>=50)and(score_Japanese>=50)and(score_English>=50))):
    print("合格",end="")
else:
    print("不合格",end="")

if((score_math>=70 and score_Japanese>=70 and score_math>=50) or (score_math+score_Japanese+score_English>=220)):
   if((score_math>=50)and(score_Japanese>=50)and(score_English>=50)):
    print("合格",end="")
else:
    print("不合格",end="")