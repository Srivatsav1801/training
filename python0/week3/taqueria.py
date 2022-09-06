def main():
    order()


def order():
    menu = {
        "baja_taco": 4.00,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super_burrito": 8.50,
        "super_quesadilla": 9.50,
        "taco": 3.00,
        "tortilla_salad": 8.00
    }
    total = 0
    while True:
        try:
            item = input("Item:").lower().replace(" ","_")
            if item in menu:
                total = total + menu[item]
                print("Total:${:.2f}".format(total))
        except EOFError:
            print()
            break


if __name__ == '__main__':
    main()
