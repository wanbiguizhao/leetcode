
from DateAndTime import code 
import pytest 

def test_is_leap_year():
    dat=code.DateAndTime()
    assert dat.is_leap_year(400)==True
    assert dat.is_leap_year(500)==False
    assert dat.is_leap_year(504) ==True
    assert dat.is_leap_year(503) ==False

def test_get_nearest_leap_year():
    dat=code.DateAndTime()
    assert dat.get_nearest_leap_year(2000)==2000
    assert dat.get_nearest_leap_year(2001)==2000
    assert dat.get_nearest_leap_year(2002)==2004
    assert dat.get_nearest_leap_year(2003)==2004
    assert dat.get_nearest_leap_year(2004)==2004

def test_calculate_leap_year_num():
    dat=code.DateAndTime()
    assert dat.calculate_leap_year_num(1999,2001)==1
    assert dat.calculate_leap_year_num(2000,2000)==0
    assert dat.calculate_leap_year_num(2000,2001)==1
    assert dat.calculate_leap_year_num(2000,2004)==1
    assert dat.calculate_leap_year_num(2000,2005)==2

if __name__ == "__main__":
    test_is_leap_year()