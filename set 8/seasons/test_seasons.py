from datetime import date
from seasons import cal


def test_cal():
    assert cal(date(1999, 1, 1), date(2000, 1, 1)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert cal(date(2001, 1, 1), date(2003, 1, 1)) == "One million, fifty-one thousand, two hundred minutes"
    assert cal(date(1995, 1, 1), date(2000, 1, 1)) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    assert cal(date(2020, 6, 1), date(2032, 1, 1)) == "Six million, ninety-two thousand, six hundred forty minutes"