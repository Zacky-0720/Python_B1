import sys
args=sys.argv
#リストを追加
animal_list=["giraffe","tiger","zebra","elephant","lion"]
#第二引数の番号の位置に、第三引数の文字列を追加
animal_list.insert(int(args[1]),args[2])
#末尾の要素を消去
#del animal_list[-1]でもOK
#animal_list.popでもOK
del animal_list[len(animal_list)-1]

#昇順に並べ替え
animal_list.sort()
#結果を出力
print(animal_list,end="")