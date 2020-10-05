import datetime
import calendar
from enum import IntEnum

class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def meetup_date(year, month, nth=None, weekday=None):
    day = 1

    if weekday is None:
        nth = 4
        weekday = 3

    if nth < 0:
        nth_mod = nth * -1
        day = calendar.monthrange(year, month)[1]
        calendar_day = datetime.date(year, month, day)
        while calendar_day.weekday() != weekday:
            day -= 1
            calendar_day = datetime.date(year, month, day)
        return datetime.date(year, month, day - (nth_mod-1) * 7)

    else:
        calendar_day = datetime.date(year, month, day)
        while calendar_day.weekday() != weekday:
            day += 1
            calendar_day = datetime.date(year, month, day)
        return datetime.date(year, month, day + (nth-1) * 7)


