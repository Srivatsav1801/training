def main():
    word = input("Input:")
    omit(word)


def omit(word):
    for _ in word:
        if _ not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            print(_, end="")


if __name__ == '__main__':
    main()
