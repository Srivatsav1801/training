from validator_collection import checkers


def main():
    email = input("What's your email address? ").strip()
    validate = is_valid(email)
    print(validate)


def is_valid(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"


if __name__ == '__main__':
    main()
