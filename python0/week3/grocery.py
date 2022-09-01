def main():
    grocery()


def grocery():
    list = {}
    while True:
        try:
            item = input()
        except EOFError:
            for item in sorted(list.keys()):
                print(list[item], item)
            break
        if item in list:
            list[item] += 1
        else:
            list[item] = 1


if __name__ == '__main__':
    main()
