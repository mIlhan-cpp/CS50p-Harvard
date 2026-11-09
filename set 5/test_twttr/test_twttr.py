from twttr import shorten

def test():
    assert shorten("Twitter")=='Twttr'

def test_num():
    assert shorten("1234")=='1234'

def test_exp():
    assert shorten('hello!')=='hll!'

def test_caps():
    assert shorten('ASDFG')=="SDFG"