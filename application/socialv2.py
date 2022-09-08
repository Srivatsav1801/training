import sys
from validator_collection import checkers
from datetime import date
import re
import csv
import pandas as pd


class Signup:
    def __init__(self):
        self.name = ""
        self.dob = ""
        self.gender = ""
        self.email = ""
        self.password = ""
        self.age = 0

    def m_signup(self):
        self.name = input("Name: ")
        self.gender = input("Gender: ")
        self.dob = input("Date of Birth: ")
        self.email = self.e_valid()
        self.password = self.p_valid()
        self.age = input("Age :")
        try:
            with open("Credentials.csv", "a") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["Name", "Gender", "Dob", "Age", "email", "password"]
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
            with open("Credentials.csv", "w") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["Name", "Gender", "Dob", "Age", "email", "password"]
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
                    break
            except ValueError:
                continue

    def p_valid(self):
        self.password = input("Password: ")
        while True:
            try:
                if len(self.password) < 6 or len(self.password) > 12:
                    break
                elif not re.search("[a-z]", self.password):
                    break
                elif not re.search("[0-9]", self.password):
                    break
                elif not re.search("[A-Z]", self.password):
                    break
                elif not re.search("[$#@]", self.password):
                    break
                else:
                    return self.password
            except ValueError:
                continue


class Signin:
    def __init__(self):
        self.email = ""
        self.password = ""

    def m_signin(self):
        self.email = input("Email address: ")
        self.password = input("Password: ")
        i = 0
        with open("Credentials.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[-2] == self.email and row[-1] == self.password:
                    print("logged in ")
                    i = 1
                    break
            if i == 0:
                print("incorrect email or password")


class Users:
    def __init__(self):
        self.name = ""
        self.no_friends = 0
        self.status = ""
        self.post = ""
        self.like = 0

    def p(self):
        self.post = input("Write something that you want to post: ")
        try:
            with open("post.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["Post", "Name", "Likes", "Date"])
                writer.writerow(
                    {"Post": self.post, "Name": self.name, "likes": 0, "Date": date.today()})
        except FileNotFoundError:
            with open("post.csv", "w") as file:
                writer = csv.DictWriter(file, fieldnames=["Post", "Name", "Likes", "Date"])
                writer.writerow(
                    {"Post": self.post, "Name": self.name, "likes": 0, "Date": date.today()})


    def homepage(self):
        choice = int(input("Sort by 1.Likes 2.Date"))
        i = 0
        if choice == 1:
            try:
                df = pd.read_csv('post.csv', names=['a', 'b', 'c', 'd'])
                df = df.sort_values('c', ascending=False)
                df = df.reset_index(drop=True)
                print(df)
            except FileNotFoundError:
                print("No Post yet")
                i = 1


        elif choice == 2:
            try:
                df = pd.read_csv('post.csv', names=['a', 'b', 'c', 'd'])
                df = df.sort_values('d', ascending=False)
                df = df.reset_index(drop=True)
                print(df)
            except FileNotFoundError:
                print("No Post yet")
                i = 1

        if(i!=1):
            select_post = int(input("Enter the post you want to like: "))
            df = pd.read_csv("post.csv")
            like = int(df.iloc[select_post]["Likes"])
            df.loc[select_post] = like + 1
            df.to_csv("post.csv", index=False)
            print(f"you liked the {select_post} post")


    def timeline(self):
        while True:
            try:
                choice = int(
                    input(
                        "Choose your option:\n1.check your timeline \n2.someone else time line:"
                    )
                )
                if choice == 2:
                    print("You chose to see someone else's timeline")
                    self.name = input("Enter the user's name")
                    break
                elif choice == 1:
                    print("You chose to see your Dateline")
                    break
            except EOFError:
                print()
                break
        timeline = []
        with open("post.csv", "r") as F:
            ro = csv.reader(F)
            for i in ro:
                timeline.append(i)
            for i in timeline:
                if i[-2] != self.name:
                    timeline.remove(i)
            print(timeline)

    def new_friends(self):
        i = 0
        with open("Credentials.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != self.name:
                    print(f"{row[0]}")
                    i += 1

        f = input("With who do you want to be friends with:")
        try:
            with open("friends.csv", "a") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["Name", "Friends"]
                )
                writer.writerow(
                    {
                        "Name": name,
                        "Friends": f
                    }
                )
        except FileNotFoundError:
            with open("friends.csv", "w") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["Name", "Friends"]
                )
                writer.writerow(
                    {
                        "Name": name,
                        "Friends": f
                    }
                )
        result = {}

        with open('friends.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                if row[0] in result:
                    result[row[0]].append(row[1])
                else:
                    result[row[0]] = [row[1]]

        for key, value in result.items():
            if key == self.name:
                print(*value, sep=",")

    def friends(self):
        find = input("Enter the name of the user to find their friends: ")
        with open("friends.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == kname:
                    print(row[1], end=",")


def main():
    new = Signup()
    old = Signin()
    feed = Users()
    q = 1
    while q == 1:
        q = 0
        choice = int(input("Choose your option\n1,Signup\n2.Signin\n"))
        if (choice == 1):
            print("you chose to Signup:")
            q = 0
            new.m_signup()
            feed.homepage()
            while True:
                try:
                    op = int(input("Choose your option\n1.To post\n2.To see Timeline\n3.To add new friend\n4.Check friends list\n5.exit"))
                    if op == 1:
                        feed.p()
                    elif op == 2:
                        feed.timeline()
                    elif op == 3:
                        feed.new_friends()
                    elif op == 4:
                        feed.friends()
                    elif op == 5:
                        sys.exit()
                except ValueError:
                    continue
        elif choice == 2:
            print("You chose to sign in:")
            q=0
            old.m_signin()
            feed.homepage()
            while True:
                try:
                    op = int(input(
                        "Choose your option\n1.To post\n2.To see Timeline\n3.To add new friend\n4.Check friends list\n5.exit"))
                    if op == 1:
                        feed.p()
                    elif op == 2:
                        feed.timeline()
                    elif op == 3:
                        feed.new_friends()
                    elif op == 4:
                        feed.friends()
                    elif op == 5:
                        sys.exit()
                except ValueError:
                    continue

if __name__ == '__main__':
    main()

