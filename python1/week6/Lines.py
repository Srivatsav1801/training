import sys


def main():
    check_cmd_arg()
    try:
        file = open(sys.argv[1], 'r')
        ls = file.readlines()
    except:
        sys.exit("file doesn't exist")
    count = 0
    for line in ls:
        if check_line(line) == False:
            count += 1
    print(count)


def check_cmd_arg():
    if len(sys.argv) < 2:
        sys.exit("too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("not a python file")


def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False


if __name__ == '__main__':
    main()
