def main():
    camelcase = input("camelCase:")
    print("snake case:", end="")
    for i in camelcase:
        if i.isupper():
            print("_" + i.lower(), end="")
        else:
            print(i, end="")


if __name__ == '__main__':
    main()
