from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-6)
    jar = Jar(0)
    assert jar.capacity == 0
    assert jar.size == 0
    jar = Jar(22)
    assert jar.capacity == 22
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(-3)
    with pytest.raises(ValueError):
        jar.deposit(15)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(4)
    assert jar.size == 9


def test_withdraw():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw(2)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(4)
    jar.withdraw(3)
    assert jar.size == 0