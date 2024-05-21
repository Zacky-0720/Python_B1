import sys
from database import session
from tables import Attendnum
from sqlalchemy import desc
from datetime import datetime

args = sys.argv

date_text = args[1]

adult_count, child_count = map(int, args[2:])

seq = session.query(Attendnum).order_by(desc(Attendnum.seq)).first().seq or 0

query = Attendnum(
    date=datetime.strptime(date_text, "%Y%m%d").date(),
    seq=seq + 1,
    adult=adult_count,
    child=child_count,
)

session.add(query)
session.commit()
