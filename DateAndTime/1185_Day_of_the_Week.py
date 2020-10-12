# _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# _DAYS_BEFORE_MONTH = [-1]  # -1 is a placeholder for indexing purposes.
# dbm = 0
# for dim in _DAYS_IN_MONTH[1:]:
#     _DAYS_BEFORE_MONTH.append(dbm)
#     dbm += dim
# del dbm, dim

# def _is_leap(year):
#     "year -> 1 if leap year, else 0."
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def _days_before_year(year):
#     "year -> number of days before January 1st of year."
#     y = year - 1
#     return y*365 + y//4 - y//100 + y//400

# def _days_in_month(year, month):
#     "year, month -> number of days in that month in that year."
#     assert 1 <= month <= 12, month
#     if month == 2 and _is_leap(year):
#         return 29
#     return _DAYS_IN_MONTH[month]

# def _days_before_month(year, month):
#     "year, month -> number of days in year preceding first day of month."
#     assert 1 <= month <= 12, 'month must be in 1..12'
#     return _DAYS_BEFORE_MONTH[month] + (month > 2 and _is_leap(year))

# def _ymd2ord(year, month, day):
#     "year, month, day -> ordinal, considering 01-Jan-0001 as day 1."
#     assert 1 <= month <= 12, 'month must be in 1..12'
#     dim = _days_in_month(year, month)
#     assert 1 <= day <= dim, ('day must be in 1..%d' % dim)
#     return (_days_before_year(year) +
#             _days_before_month(year, month) +
#             day)
class Solution:
    def __init__(self):
        self._DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dbm=0
        self._DAYS_BEFORE_MONTH=[-1]
        for dim in self._DAYS_IN_MONTH[1:]:
            self._DAYS_BEFORE_MONTH.append(dbm)
            dbm=dbm+dim
        del dbm ,dim
    def _is_leap_year(self,year:int):
        return year%4==0 and (year % 100 != 0 or year % 400 == 0)
    
    def _days_before_year(self,year):
        y=year-1 
        return y*365+ y//4 -y//100 +y//400
    
    def _days_before_month(self,year,month):
        # return self._DAYS_BEFORE_MONTH[month]+1 if ( month>2 and self._is_leap_year(year)) else 0
        if month>2 and self._is_leap_year(year):
            return  self._DAYS_BEFORE_MONTH[month]+ 1 
        return  self._DAYS_BEFORE_MONTH[month]

    def _ymd2ord(self,year,month,day):
        return self._days_before_year(year)+self._days_before_month(year,month)+day

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        answer_chioce=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        basic_index=0
        
        basic_days=  737681#self._ymd2ord(2020,9,13)
        print(basic_days)
        target_days=self._ymd2ord(year,month,day)
        x_days_index=(target_days-basic_days+basic_index)%7
        #print(x_days_index)
        return answer_chioce[x_days_index]



if __name__ == "__main__":
    s=Solution()
    print(s.dayOfTheWeek(31,8,2019))

        