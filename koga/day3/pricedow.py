import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]          #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")      #果物類をタプルで定義
alcohol = ("ビール", "日本酒")               #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く
#タプルに第２引数を反映させる。
category={"果物類":fruits,"酒類":alcohol,"麺類":noodles}
# category[hm_class]→値引き対象のカテゴリにある商品
# hinmoku[category[hm_class][i]]→全商品の辞書型の中で、値引きカテゴリに入った商品i番目の価格

#タプルに入った商品一つ一つの価格を値引く。
for i in range(len(category[hm_class])):
    # 対象商品から第３引数の値下げを実行(23と24は同じ)
    hinmoku[category[hm_class][i]]-=price_down
    # hinmoku[category[hm_class][i]]=hinmoku[category[hm_class][i]]-=price_down-price_down
    # 1円未満のものを1円に設定
    if hinmoku[category[hm_class][i]]<1:
        hinmoku[category[hm_class][i]]=1

print(hinmoku,end="")