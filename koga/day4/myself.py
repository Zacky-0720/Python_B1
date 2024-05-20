#引数の引き渡し
import sys
from introduce import Intro
args=sys.argv

#インスタンスの生成
#「Intro」というクラスは"def __init__(self, name, age):"name ageという枠がある
#「Intro」というクラス内にargs[1],args[2]を挿入した変数として「outtext」を定義した。
outtext = Intro(args[1],args[2])

#名前、年齢の出力
print(outtext.name_out())
print(outtext.age_out())

