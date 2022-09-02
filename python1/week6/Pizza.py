import sys
import csv
from tabulate import tabulate


def main():
    check_cmd_arg()
    table = []
    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    except:
        sys.exit("file doesn't exist")
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


def check_cmd_arg():
    if len(sys.argv) < 2:
        sys.exit("too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("not a csv file")


if __name__ == '__main__':
    main()
