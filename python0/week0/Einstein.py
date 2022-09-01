def main():
    m = input("m:")
    e = cal(m)
    print(f"E:{e}")


def cal(m):
    c = 300000000
    value = m * (c ** 2)
    return value


main()
