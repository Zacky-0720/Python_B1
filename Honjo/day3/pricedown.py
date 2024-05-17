import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く
if hm_class=='果物類':
    for fruit in fruits:
        price_after_price_down=hinmoku[fruit]-price_down
        if price_after_price_down<1:
            price_after_price_down=1
        hinmoku[fruit]=price_after_price_down
elif hm_class=='酒類':
    for drink in alcohol:
        price_after_price_down=hinmoku[drink]-price_down
        if price_after_price_down<1:
            price_after_price_down=1
        hinmoku[drink]=price_after_price_down
else:
    for noodle in noodles:
        price_after_price_down=hinmoku[noodle]-price_down
        if price_after_price_down<1:
            price_after_price_down=1
        hinmoku[noodle]=price_after_price_down
print(hinmoku,end="")
