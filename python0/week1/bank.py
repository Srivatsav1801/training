def main():
    greet = input("Greeting: ").lower()
    amt = check(greet)
    print(f"${amt}")


def check(greet):
    if greet == "hello":
        return 0
    elif greet[0] == "h":
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()
