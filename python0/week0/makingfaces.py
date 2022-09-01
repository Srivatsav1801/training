def main():
    msg = input("Enter the message:")
    new_msg = convert(msg)
    print(new_msg)


def convert(msg):
    emoji = msg.replace(":)", "😊").replace(":(", "😟")
    return emoji


main()
