import random


def main():
    game()


def game():
    while True:
        try:
            level = int(input("level: "))
            if level > 0:
                break
        except:
            pass

    random_no = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < random_no:
                print("too small!")
            elif guess > random_no:
                print("too large!")
            else:
                print("just right!")
                break
        except:
            pass


if __name__ == '__main__':
    main()
