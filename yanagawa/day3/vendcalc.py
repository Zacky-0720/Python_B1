def main():
    item_dict = {"お茶": 110, "コーヒー": 100, "ソーダ": 160, "コーンポタージュ": 130}

    for k, v in item_dict.items():
        print(f"{k}：{v}円")

    money = 0
    while True:
        try:
            money = int(input("投入金額を入力してください："))
            if money > 10000:
                print(
                    "10,000円を超える金額は投入できません。再度投入金額を入力してください"
                )
                continue
            if money < 0:
                print("負の値は入力できません。再度投入金額を入力してください")
                continue
            if len(get_buyable_item(item_dict, money)) == 0:
                print(
                    f"{money}円では購入できる商品がありません。再度投入金額を入力してください"
                )
                continue
            if money % 10 != 0:
                print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
                continue
            break
        except ValueError:
            print("数値以外が入力されました。再度投入金額を入力してください")
            continue

    while True:
        buyable_item_dict = get_buyable_item(item_dict, money)
        for k, v in buyable_item_dict.items():
            print(f"{k}：{v}円")

        result = buy(buyable_item_dict, money)
        if not result["is_continue"]:
            break

        money = result["money"]


def get_buyable_item(item_dict, money):
    """引数に渡した金額で購入可能な商品の辞書を返す関数"""
    filtered_dict = {k: v for k, v in item_dict.items() if v <= money}
    return filtered_dict


def buy(item_dict, money):
    """購入処理を行う関数"""
    purchase_item = input("何を購入しますか(商品名/cancel)：")
    if purchase_item == "cancel":
        change_dict = calc_change(money)
        print_change(change_dict)
        return {"is_continue": False, "money": money}
    if purchase_item not in item_dict.keys():
        print("その商品は購入できません")
        return {"is_continue": True, "money": money}

    money -= item_dict[purchase_item]
    if money == 0:
        return {"is_continue": False, "money": money}

    buyable_item_dict = get_buyable_item(item_dict, money)
    if len(buyable_item_dict) == 0:
        change_dict = calc_change(money)
        print_change(change_dict)
        return {"is_continue": False, "money": money}

    is_continue = ""
    while True:
        print(f"残金：{money}円")
        is_continue = input("続けて購入しますか(Y/N)：")
        if is_continue == "Y" or is_continue == "N":
            break
        print("YかNを入力してください")

    if is_continue == "N":
        change_dict = calc_change(money)
        print_change(change_dict)
        return {"is_continue": False, "money": money}

    return {"is_continue": True, "money": money}


def calc_change(money):
    """おつりを計算する関数"""
    coins = (5000, 2000, 1000, 500, 100, 50, 10)
    result = {}

    money_tmp = money

    for coin in coins:
        result[coin] = money_tmp // coin
        money_tmp = money_tmp % coin

    filtered_result = {k: v for k, v in result.items() if v != 0}
    return filtered_result


def print_change(change_dict):
    """おつりをフォーマットに沿って出力する関数"""
    print("おつり")
    for k, v in change_dict.items():
        print(f"{k}円{'札' if k >= 1000 else '玉'}：{v}枚")


main()
