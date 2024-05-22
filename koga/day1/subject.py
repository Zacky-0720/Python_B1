import sys
args=sys.argv

#点数の入力
score_math=int(args[1])
score_Japanese=int(args[2])
score_English=int(args[3])

if(((score_math>=70 and score_Japanese>=70 and score_math>=50) or (score_math+score_Japanese+score_English>=220)) and ((score_math>=50)and(score_Japanese>=50)and(score_English>=50))):
    print("合格",end="")
else:
    print("不合格",end="")

#条件1：各科目70点以上または合計点220以上
if((score_math>=70 and score_Japanese>=70 and score_math>=50) or (score_math+score_Japanese+score_English>=220)):
   #条件2：全科目が50点以上
   if((score_math>=50)and(score_Japanese>=50)and(score_English>=50)):
    print("合格",end="")
else:
    print("不合格",end="")