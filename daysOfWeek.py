def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    # reference year 1900/1/1 - Monday

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # leap year: a year dividable by 4, and not dividiable by 100 or is dividable by 400
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days_since_ref = 0

    for y in range(1900, year):  # uninclusive
        if is_leap(y):
            days_since_ref += sum(days_in_month_leap)
        else:
            days_since_ref += sum(days_in_month)

    for m in range(1, month):
        if is_leap(year):
            days_since_ref += days_in_month_leap[m - 1]
        else:
            days_since_ref += days_in_month[m - 1]

    days_since_ref += day - 1

    return days[days_since_ref % 7]
