def main():
    time = str(input("What time is it?"))
    ml = convert(time)
    if 8.00 >= ml >= 7.00:
        print("breakfast time")
    elif 13.00 >= ml <= 12.00:
        print("lunch time")
    elif 19.00 >= ml <=18.00:
        print("dinner time")
    else:
        print("work time") 


def convert(time):
    hrs, min = time.split(":")
    hours = int(hrs) + (int(min)/60)
    print(hours)
    return hours 
    


if __name__ == "__main__":
    main()
