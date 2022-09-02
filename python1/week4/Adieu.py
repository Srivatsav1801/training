import inflect
def main():
    adieu()

def adieu():
    i = inflect.engine()
    n = []
    while True:
        try:
            name = input("Name: ")
            n.append(name)
        except EOFError:
            print()
            break
    op = i.join(n)
    print("Adieu, adieu, to " +op)

if __name__ == '__main__':
    main()