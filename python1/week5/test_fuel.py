from fuel import convert, gauge
import pytest


def main():
    test_input1()
    test_zero_division()
    test_value()


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value():
    with pytest.raises(valueError):
        convert("dog/cat")


def test_input1():
    assert convert('4/4') == 100.0 and gauge(100) == "F"
    assert convert('2/4') == 50.0 and gauge(0.5) == "50%"
    assert convert('1/4') == 25.0 and gauge(0.25) == "25%"
    assert convert('3/4') == 75.0 and gauge(0.75) == "75%"
    assert convert('0/4') == 0.0 and gauge(0) == "E"


if __name__ == '__main__':
    main()
