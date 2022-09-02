from Twttr import shorten
def main():
    test_twttr()


def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("Hello World") =="Hll Wrld"

if __name__ == '__main__':
    main()
