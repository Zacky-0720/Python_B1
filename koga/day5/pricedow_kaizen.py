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

#値引き対象のカテゴリにある商品
# hinmoku[discount_product[i]]→全商品の辞書型の中で、値引きカテゴリに入った商品i番目の価格
print("元値："+str(hinmoku))

#タプルに入った商品一つ一つの価格を値引く。
def pricedown(discount_price,discount_category):
    #値引き対象のカテゴリにある商品を変数「discount_category」に格納
    discount_product=category[discount_category]
    for i in range(len(discount_product)):
    # 対象商品から第３引数の値下げを実行
        hinmoku[discount_product[i]]-=discount_price
    # 1円未満のものを1円に設定
        if hinmoku[discount_product[i]]<1:
            hinmoku[discount_product[i]]=1
    #値引き後の商品リストを返り値に設定
    return hinmoku

#値引きの実施
V=pricedown(price_down,hm_class)
print("値引き後価格："+str(V))


#変更点
#category[hm_class]をdiscount_productに変更し、可読性の向上
#値下げ対象品のリスト作成と値下げを関数(pricedown)に格納。第二引数と第三引数の入力によって実行可能にする。
#値引き前のリストを表示
