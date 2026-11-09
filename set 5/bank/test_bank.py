from bank import value

def test_nil():
    assert value('Hello')==0
def test_mid():
    assert value('hsss')==20
def test_max():
    assert value('aHelLo')==100
    assert value('100')==100
