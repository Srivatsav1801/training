import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe", s):
        url = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url:
            s_url = url.groups()
            return "https://youtu.be/" + s_url[3]


if __name__ == "__main__":
    main()
