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

    randomno = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < randomno:
                print("too small!")
            elif guess > randomno:
                print("too large!")
            else:
                print("just right!")
                break
        except:
            pass
if __name__ == '__main__':
    main()
