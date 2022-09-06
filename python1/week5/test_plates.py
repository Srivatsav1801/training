from plates import is_valid


def main():
    test_is_valid1()
    test_is_valid2()
    test_is_valid3()
    test_is_valid4()


def test_is_valid1():
    assert is_valid("hello12") == False
    assert is_valid("John") == True
    assert is_valid("123") == False


def test_is_valid2():
    assert is_valid("CS05") == False
    assert is_valid("  50") == False
    assert is_valid("CS50P") == False


def test_is_valid3():
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("hola") == True



def test_is_valid4():
    assert is_valid("PI3.14") == False
    assert is_valid("re.verse") == False


if __name__ == '__main__':
    main()
