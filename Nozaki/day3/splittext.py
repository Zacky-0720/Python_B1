# 第1引数を受け取る
import sys
intext = sys.argv[1]
# 第2引数を受け取る
place = int(sys.argv[2])

# 第1引数を区切る
splittext = intext.split()
# n番目（第2引数）の取得
receive = place - 1
# プリントする
print(splittext[receive], end="")
