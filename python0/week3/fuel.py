def main():
    amt = input("Fraction:")
    fuel(amt)


def fuel(amt):
    while True:
        try:
            n, m = amt.split("/")
            f = int(n) / int(m)
            if n > m:
                continue
            break
        except(ValueError, ZeroDivisionError):
            continue

    p = f * 100
    if p <= 1:
        print("E")
    elif p >= 99:
        print("F")
    else:
        print("{:.2f}%".format(p))


if __name__ == '__main__':
    main()
