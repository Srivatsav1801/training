def main():
    word = input("Input:")
    print("Output:", shorten(word))


def shorten(word):
    shortw = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            shortw += letter
    return shortw


if __name__ == '__main__':
    main()
