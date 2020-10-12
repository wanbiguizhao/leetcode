class DateAndTime:
    """
    日期处理的常用类
    """
    def is_leap_year(self,year:int):
        """
        [judge year is leap year or not]

        Args:
            year (int): [year]

        Returns:
            [bool]: [input year is leap year return true ]
        """        
        if year<1:
            return False
        if year%100==0:
            return year%400==0
        else:
            return year%4==0
    def get_nearest_leap_year(self,year:int):
        """
        [ function return  a leap year which is nearest for the input year]

        Args:
            year (int): [description]
        """
        k=0
        while k<4:
            if self.is_leap_year(year+k):
                return year+k 
            if self.is_leap_year(year-k):
                return year-k
            k=k+1
    def calculate_leap_year_num(self,beg_year,end_year):
        """
        [ how many leap year from beg_year to end_year .  [beg_year,end_year) ]

        Args:
            beg_year ([type]): [description]
            end_year ([type]): [description]
        """
        min_leap_year=self.get_nearest_leap_year(beg_year)
        if end_year-min_leap_year>0:
            return 1+(end_year-min_leap_year-1)//4
        return 0
    
    def calculate_internal_days(self):
        

    def 
if __name__ == "__main__":
    pass
