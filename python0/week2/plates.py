def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>2 and len(s)<6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    i=0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return false
            else:
                break
        i = i + 1
    for q in s:
        if q in ['.',' ','!','?']:
            return False
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
    return True
main()