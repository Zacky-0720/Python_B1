from database import session
from tables import Holiday

# データを取得する
holidaylist=session.query(Holiday).all()
#query().all()→「SELECT * FROM HOliday」と同じ、すべての行を射影するもの。

for holiday in holidaylist:
    print(holiday.holi_date,holiday.holi_text)
