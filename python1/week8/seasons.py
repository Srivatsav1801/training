from datetime import date
import sys
import re
import inflect

p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    try:
        y, m, d = chk(birth_date)
    except:
        sys.exit("Invalid Date")
    dob = date(int(y), int(m), int(d))
    dot = date.today()
    no_of_days = dot - dob
    total_time = no_of_days.days * 24 * 60
    op = p.number_to_words(total_time,andword="")
    print(op.capitalize() + " minutes")


def chk(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        y, m, d = birth_date.split("-")
        return y, m, d


if __name__ == "__main__":
    main()
