def main():
    msg = input("Enter the Message:")
    new_msg = cap_to_low(msg)
    print(f"{new_msg}")


def cap_to_low(msg):
    low_msg = msg.lower()
    return low_msg


if __name__ == '__main__':
    main()
