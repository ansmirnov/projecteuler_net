__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from datetime import date
from dateutil.relativedelta import relativedelta

tdate = date(1901, 01, 01)
enddate = date(2000, 12, 31)
cnt = 0
while tdate < enddate:
    if tdate.weekday() == 6:
        cnt += 1
    tdate = tdate + relativedelta(months=1)

print cnt