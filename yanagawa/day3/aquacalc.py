import sys
import datetime

args = sys.argv

date = args[1]
adult_count = int(args[2])
child_count = int(args[3])

adult_price_dict = {"workday": 2000, "holiday": 2400}
child_price_dict = {"workday": 1200, "holiday": 1500}

t = datetime.datetime.strptime(date, "%Y%m%d")

is_holiday = t.strftime("%w") in ("0", "6")
price_state = "holiday" if is_holiday else "workday"

adult_price_sum = adult_price_dict[price_state] * adult_count
child_price_sum = child_price_dict[price_state] * child_count


price_sum = adult_price_sum + child_price_sum

print(price_sum, end="")
