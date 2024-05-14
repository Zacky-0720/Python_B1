import sys


def main():
    args = sys.argv

    math_score = int(args[1])
    japanese_score = int(args[2])
    english_score = int(args[3])

    if math_score >= 70 and japanese_score >= 70 and english_score >= 70:
        print("合格", end="")
        return

    if math_score < 50 or japanese_score < 50 or english_score < 50:
        print("不合格", end="")
        return

    score_sum = math_score + japanese_score + english_score
    if score_sum >= 220:
        print("合格", end="")
        return

    print("不合格", end="")


main()
