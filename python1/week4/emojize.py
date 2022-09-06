import emoji

def main():
    em = input("Input: ")
    emote(em)

def emote(em):
    print(emoji.emojize(em,language="alias"))

if __name__ == '__main__':
    main()