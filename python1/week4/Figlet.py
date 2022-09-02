import random
import sys


def main():
    pf()


def pf():
    from pyfiglet import Figlet
    figlet = Figlet()
    if len(sys.argv) == 1:
        israndomfont = True
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font"):
        israndomfont = False
    else:
        # print("Invalid usage")
        sys.exit(1)

    figlet.getFonts()

    if israndomfont == False:
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            print("Invalid usage")
            sys.exit(1)
    else:
        font = random.choice(figlet.getFonts())

    msg = input("Input: ")
    print("Output:")
    print(figlet.renderText(msg))


if __name__ == '__main__':
    main()
