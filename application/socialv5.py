from validator_collection import checkers
from datetime import datetime
import sys
import re
import csv
import pandas as pd



class Users:
    def __init__(self):
        self.name = ""
        self.dob = ""
        self.gender = ""
        self.email = ""
        self.password = ""
        self.age = 0


    @staticmethod
    def getname():
        name_of_user = str(input("Name: "))
        return name_of_user

    def m_signup(self):
        self.name = Users.getname()
        self.gender = input("Gender: ")
        self.dob = input("Date of Birth: ")
        self.email = self.e_valid()
        self.password = self.p_valid()
        self.age = input("Age :")
        try:
            with open("credentials.csv", "a") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["Name", "Gender", "Dob", "Age", "email", "password"],
                )
                writer.writerow(
                    {
                        "Name": self.name,
                        "Gender": self.gender,
                        "Dob": self.dob,
                        "Age": self.age,
                        "email": self.email,
                        "password": self.password,
                    }
                )
        except FileNotFoundError:
            with open("credentials.csv", "w") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["Name", "Gender", "Dob", "Age", "email", "password"],
                )
                writer.writerow(
                    {
                        "Name": self.name,
                        "Gender": self.gender,
                        "Dob": self.dob,
                        "Age": self.age,
                        "email": self.email,
                        "password": self.password,
                    }
                )

    def e_valid(self):
        self.email = input("E-mail: ")
        while True:
            try:
                if checkers.is_email(self.email):
                    return self.email
                else:
                    print("invalid mail id")
                    sys.exit()
            except ValueError:
                continue


    def p_valid(self):
        self.password = input("Password: ")
        while True:
            try:
                if not re.search(
                    "^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[#?!@$%^&*-]).{6,}$",
                    self.password,
                ):
                    print("Invalid password")
                    sys.exit()
                else:
                    return self.password
            except ValueError:
                continue

    def m_signin(self):
        self.email = input("Email address: ")
        self.password = input("Password: ")
        i = 0
        try:
            with open("credentials.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[-2] == self.email and row[-1] == self.password:
                        self.name = row[0]
                        print("logged in ")
                        i = 1
                        break
                if i == 0:
                    print("incorrect email or password")
                    sys.exit()
        except FileNotFoundError:
            print("Record not found")
            sys.exit()


class Home:
    def __init__(self):
        self.name= Users.getname()
        self.no_friends = ""
        self.post = ""
        self.like = 0

    def new_post(self):
        self.post = input("Write something that you want to post: ")
        now = datetime.now()
        try:
            with open("post.csv", "a") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["Post", "Name", "Likes", "Date"]
                )
                writer.writerow(
                    {
                        "Post": self.post,
                        "Name": self.name,
                        "Likes": 0,
                        "Date": now.strftime("%d/%m/%Y %H:%M:%S"),
                    }
                )
        except FileNotFoundError:
            with open("post.csv", "w") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["Post", "Name", "Likes", "Date"]
                )
                writer.writerow(
                    {
                        "Post": self.post,
                        "Name": self.name,
                        "Likes": 0,
                        "Date": now.strftime("%d/%m/%Y %H:%M:%S"),
                    }
                )

    def homepage(self):
        choice = int(input("Sort by 1.Likes 2.Date"))
        i = 0
        if choice == 1:
            try:
                df = pd.read_csv("post.csv", names=["a", "b", "c", "d"])
                df = df.sort_values("c", ascending=False)
                df = df.reset_index(drop=True)
                print(df)
            except FileNotFoundError:
                print("No Post yet")
                i = 1

        elif choice == 2:
            try:
                df = pd.read_csv("post.csv", names=["a", "b", "c", "d"])
                df["d"] = pd.to_datetime(df["d"])
                df = df.sort_values("d", ascending=False)
                df = df.reset_index(drop=True)
                print(df)
            except FileNotFoundError:
                print("No Post yet")
                i = 1

        if i != 1:
            select_post = int(input("Enter the post you want to like: "))
            df.loc[select_post, "c"] += 1
            df.to_csv("post.csv", index=False, header=False)
            print(f"you liked the {select_post} post")

    def timeline(self):
        while True:
            try:
                choice = int(
                    input(
                        "Choose your option:\n1.check your timeline \n2.someone else time line:\n "
                    )
                )
                if choice == 2:
                    print("You chose to see someone else's timeline")
                    u_name = str(input("Enter the user's name: "))
                    break
                elif choice == 1:
                    print("You chose to see your timeline")
                    u_name = self.name
                    break
            except EOFError:
                print()
        timeline = []
        with open("post.csv", "r") as F:
            ro = csv.reader(F)
            for i in ro:
                timeline.append(i)
            for items in timeline:
                d = items
                if d[1] == str(u_name):
                    print(
                        f"{d[0]} by {d[1]}, no of likes:{d[2]},Date of posting:{d[3]}"
                    )

    def new_friends(self):
        i = 0
        with open("credentials.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != str(self.name):
                    print(f"{row[0]}")
                    i += 1

        f = input("With who do you want to be friends with:")
        try:
            with open("friends.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Friends"])
                writer.writerow({"Name": self.name, "Friends": f})
        except FileNotFoundError:
            with open("friends.csv", "w") as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Friends"])
                writer.writerow({"Name": self.name, "Friends": f})
        result = {}

        with open("friends.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in csvreader:
                if row[0] in result:
                    result[row[0]].append(row[1])
                else:
                    result[row[0]] = [row[1]]

        for key, value in result.items():
            if key == self.name:
                print(*value, sep=",")

    def friends(self):
        op = int(
            input(
                "Choose your option:\n1.To check your friends\n2.To check another user's friends:\n"
            )
        )
        if op == 1:
            find = self.name
        elif op == 2:
            find = input("Enter the name of the user to find their friends: ")
        else:
            print("option does not exist\n")
            sys.exit()
        with open("friends.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(find):
                    print(row[1], end=",")


def main():
    log = Users()
    app = Home()
    while True:
        try:
            choice = int(input("Choose your option\n1,Signup\n2.Signin\n"))
            if choice == 1:
                print("you chose to Signup:")
                log.m_signup()
            elif choice == 2:
                print("You chose to sign in:")
                log.m_signin()
            app.homepage()
            while True:
                try:
                    op = int(
                        input(
                            "Choose your option\n1.To post\n2.To see Timeline\n3.To add new friend\n4.Check friends list\n5.Homepage\n6.exit\n"
                        )
                    )
                    if op == 1:
                        app.new_post()
                    elif op == 2:
                        app.timeline()
                    elif op == 3:
                        app.new_friends()
                    elif op == 4:
                        app.friends()
                    elif op == 5:
                        app.homepage()
                    elif op == 6:
                        sys.exit()
                except ValueError:
                    continue
        except ValueError:
            continue


if __name__ == "__main__":
    main()
