def main():
    time = str(input("What time is it? "))
    ml = convert(time)
    if 7.00 <= ml <= 8.00:
        print("breakfast time")
    elif 12.00 <= ml <= 13.00:
        print("lunch time")
    elif 18.00 <= ml <= 19.00:
        print("dinner time")
    else:
        return 0


def convert(time):
    hours, minutes = time.split(":")
    t = int(hours) + (int(minutes) / 60)
    return t


if __name__ == "__main__":
    main()
