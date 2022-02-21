# -*- coding: utf-8 -*-
import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    return bool(isleap(year))


# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2:
        return 28


name = input("input your name: ")
age = input("input your age: ")
localtime = time.localtime(time.time())

year = int(age)
begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

month = year * 12 + localtime.tm_mon
day = sum(
    366 if (judge_leap_year(y)) else 365 for y in range(begin_year, end_year)
)

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day += month_days(m, leap_year)

day += localtime.tm_mday
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
