def main():
    msg = input("Enter the msg:")
    nmsg = pbspeed(msg)
    print(nmsg)


def pbspeed(msg):
    sl = msg.replace(" ", "...")
    return sl


if __name__ == '__main__':
    main()
