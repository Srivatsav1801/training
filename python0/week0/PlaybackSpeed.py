
def main():
    msg = input("Enter the msg:")
    nmsg = pbspeed(msg)
    print(nmsg)
def pbspeed(msg):
    sl = msg.replace(" ","...")
    return sl

main()