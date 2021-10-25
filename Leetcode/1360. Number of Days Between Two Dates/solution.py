class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap_year(year: int):
            return True if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) else False

        def count_days_date(date: str):
            year, month, day = map(int, date.split("-"))
            is_leap = is_leap_year(year)
            days: int = 0

            # add days per year
            for y in range(1970, year):
                days += 366 if is_leap_year(y) else 365

            # add days per month
            for m in range(1, month):
                if m == 2:
                    days += 29 if is_leap else 28
                    continue

                if m in [1, 3, 5, 7, 8, 10]:
                    days += 31
                else:
                    days += 30

            days += day

            return days

        return abs(count_days_date(date1) - count_days_date(date2))
