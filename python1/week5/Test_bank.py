from Bank import value


def main():
    test_value1()
    test_value2()
    test_value3()


def test_value1():
    assert value("hello") == "$0"
    assert value("HELLO") == "$0"
    assert value(" Hello ") == "$0"


def test_value2():
    assert value("how is it going") == "$20"
    assert value("how can I help you?") == "$20"
    assert value("hola") == "$20"


def test_value3():
    assert value("whats up") == "$100"
    assert value("good morning") == "$100"
    assert value("good afternoon") == "$100"


if __name__ == '__main__':
    main()
