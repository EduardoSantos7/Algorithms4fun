class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        return f"{year}-{months.get(month)}-{day[:-2].zfill(2)}"
