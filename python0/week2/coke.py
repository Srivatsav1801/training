def main():
    cokeprice = 50
    pcheck(cokeprice)


def pcheck(cokeprice):
    while cokeprice > 0:
        print(f"Amount Due:{cokeprice}")
        coin = int(input("Insert Coin"))
        cokeprice = cokeprice - coin
        if cokeprice <= 0:
            print(f"Change owned:{cokeprice * (-1)}")


if __name__ == '__main__':
    main()
