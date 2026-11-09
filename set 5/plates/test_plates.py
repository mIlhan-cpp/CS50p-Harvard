from plates import is_valid


def test_len():
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True
    assert is_valid("ABCDEFG") == False

def test_strt():
    assert is_valid("AB123") == True
    assert is_valid("123ABC") == False
    assert is_valid("1ABC") == False
    assert is_valid("1A") == False
    assert is_valid("A1") == False

def test_num():
    assert is_valid("ABC123") == True
    assert is_valid("ABC12") == True
    assert is_valid("ABC123D") == False
    assert is_valid("ABC1D") == False

def test_zero():
    assert is_valid("ABC123") == True
    assert is_valid("ABC012") == False
    assert is_valid("AB0123") == False

def test_symbols():
    assert is_valid("ABC!67") == False
    assert is_valid("ABC-213") == False
    assert is_valid("FG 783") == False