def main():
    filename = input("File Name:")
    ty = ex(filename)
    print(ty)


def ex(filename):
    n, e = filename.split(".")
    if e == "gif" or e == "jpg" or e == "jpeg" or e == "png":
        return f"image/{e}"
    elif e == "pdf":
        return f"application/{e}"
    elif e == "txt":
        return f"text/{e}"
    elif e == "zip":
        return f"application/{e}"
    else:
        return "application/octet-stream"


if __name__ == '__main__':
    main()
