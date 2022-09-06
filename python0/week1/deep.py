def main():
    ans = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything ?")).lower()
    re = check(ans)
    print(re)


def check(ans):
    if ans == "42":
        return "Yes"
    elif ans == "forty-two":
        return "Yes"
    elif ans == "forty-two":
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    main()
