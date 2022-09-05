
from ast import main


def main():
    msg = input("Enter the Message:")
    nmsg = cap_to_low(msg)
    print(f"{nmsg}")
    
def cap_to_low(msg):
    low_msg = msg.lower()
    return low_msg

main()

