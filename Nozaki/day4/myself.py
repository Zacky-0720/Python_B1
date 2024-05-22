# 第１引数の取得
import sys
args = sys.argv

# 名前と年齢のクラス定義
class Intro :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def name_out(self):
        nametxt = "私の名前は" + self.name + "です"
        return nametxt
    
    def age_out(self):
        agetxt = "年齢は、" + self.age + "です"
        return agetxt

# myfamilyよりコメントアウト 
# outtext = Intro(args[1], args[2])
# a=outtext.name_out()
# print(a)

# b=outtext.age_out()
# print(b)