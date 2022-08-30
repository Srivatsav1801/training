cokeprice = 50 
while cokeprice > 0:
    print(f"Amount Due:{cokeprice}")
    coin = int(input("Insert Coin"))
    cokeprice = cokeprice - coin
    if cokeprice <= 0 :
        print(f"Change owned:{cokeprice*(-1)}") 