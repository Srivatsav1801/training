import sys
from PIL import Image, ImageOps
import os


def main():
    pic()


def pic():
    if len(sys.argv) == 3:
        extension = ['.jpg', '.jpeg', 'png']
        extension1 = os.path.splitext(sys.argv[1])
        extension2 = os.path.splitext(sys.argv[2])
        if extension[1] == extension[1] and extension[1] in extension:
            try:
                uimage = Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("File doesn't exist")
            shirt = Image.open("shirt.png")
            size = shirt.size
            uimage = ImageOps.fit(uimage, size)
            uimage.paste(shirt, shirt)
            uimage.save(sys.argv[2])
        elif extension1[1] != extension2[1]:
            sys.exit("Input and output have different extensions")
        else:
            sys.exit("Wrong extension")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command line arguments")


if __name__ == '__main__':
    main()
