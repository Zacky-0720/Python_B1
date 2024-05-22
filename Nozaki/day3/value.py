# 第1引数を受け取る
import sys  
# 第2引数を受け取る
hm_class = sys.argv[1] 

# 第3引数を受け取る 
price_down = int(sys.argv[2])   #値下げ額 
#品目（品名と価格）を辞書型で定義 
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258} 

#区分ごとの定義 
# 果物類をタプルで定義
fruits = ("リンゴ","みかん","バナナ")
# 酒類をタプルで定義
alcohol = ("ビール","日本酒")
#麺類をタプルで定義 
noodls = ("ラーメン","うどん","パスタ")
 
change = [] 
#果物類の価格変更#酒類の価格変更#麺類の価格変更     
if(hm_class == "果物類"):
    change = fruits
elif(hm_class == "酒類"):
    change = alcohol
else:
    change = noodls

# print(change)

for i in change:
    if((hinmoku[i] - price_down) <= 1):
        hinmoku[i] = 1        
    else:
        hinmoku[i] -= price_down
    
print(hinmoku)