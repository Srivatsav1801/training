import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    times = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(times)


if __name__ == "__main__":
    main()
