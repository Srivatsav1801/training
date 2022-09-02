import sys
import csv


def main():
    check_cmd_arg()
    out = []
    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nname = row["name"].split(",")
                out.append({"first": nname[1].lstrip(), "last": nname[0], "house": row["house"]})
    except:
        sys.exit(f"could not read {sys.argv[1]}")
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in out:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


def check_cmd_arg():
    if len(sys.argv) < 3:
        sys.exit("too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("too many command line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("not a csv file")


if __name__ == '__main__':
    main()
