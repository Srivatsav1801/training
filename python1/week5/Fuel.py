def main():
    amt = input("Fraction:")
    percent = convert(amt)
    gauge(percent)


def convert(amt):
    while True:
        try:
            n, m = amt.split("/")
            f = int(n) / int(m)
            if f <= 1:
                p = int(f) * 100
                return p
                break
            else:
                amt = input("Fraction:")
                pass
        except(ValueError, ZeroDivisionError):
            raise


def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return str(percent) + "%"


if __name__ == '__main__':
    main()
