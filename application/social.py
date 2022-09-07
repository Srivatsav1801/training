from validator_collection import checkers
from datetime import date
import re
import json
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
        self.dob = int(input("Date of Birth: "))
        self.email = e_valid()
        self.password = p_valid()
        self.age = input("Age :")
        with open("Credentials.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "gender", "dob", "Age", "email", "password"])
            writer.writerow({"Name": self.name, "Gender": self.gender, "Dob": self.dob, "Age": self.age, "email": self.email, "password": self.password})
        menu()

    def e_valid(self):
        self.email = input("E-mail: ")
        while True:
            try:
                if checkers.is_email(self.email):
                    continue
                else:
                    break
            except ValueError:
                continue
        return self.email

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
                    print("Valid Password")
                    break
            except ValueError:
                continue


class Signin:

    def __init__(self):
        self.email = ""
        self.password = ""

    def m_signin(self):
        self.email = input("Email address: ")
        self.password = input("Password: ")
        with open("Credentials.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[-2] == self.email and row[-1] == self.password:
                    menu()
                else:
                    print("incorrect email or password")


class Users:

    def __init__(self):
        self.name = ""
        self.no_friends = 0
        self.status = ""
        self.post = ""
        self.wall ={}
        self.like = 0

    def post(self):
        #to get the list of existing post
        """""
        with open("post.csv") as file:
            for line in file:
                row = line.rstrip().split(",")
                print(f"Post: {row[0]} by {row[1]} no of likes:{row[2]}")

        with open("Post.csv", 'r') as fp:
            for line in fp:
                x = line[:-1]
                self.wall.append(x)
        """
        #get the post info from user
        self.post = input("Write something that you want to post: ")
        self.wall.append(post)
        with open("post.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Post", "Name", "Likes", "Time"])
            writer.writerow({"Post": self.post, "Name": self.name, "likes": 0 , "Time" : date.today()})

    def homepage(self):
        """""
        with open("post.csv") as file:
            for line in file:
                row = line.rstrip().split(",")
                print(f"{int(line) + 1 }Post: {row[0]} by {row[1]} no of likes:{row[2]}")
        """
        posts = []

        with open("post.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                posts.append({"Post": row["Post"], "Name": row["Name"],"Likes":row["Likes"],"Time":row["Time"]})


        for post in sorted(posts, key=lambda post: post["Likes"]):
            print(f"{post['Post']} by {post['Name']} no of likes:{post['Likes']} date of post{post['Time']}")
            choice = int(input("Enter the post you want to like: "))
            df = pd.read_csv("post.csv")
            like = int(df.iloc[choice]["Likes"])
            df.loc[choice - 1 , 'Likes'] = like + 1
            df.to_csv("post.csv", index=False)
            print(f"you liked the {choice} post")

    def timeline(self):
        while True:
            try:
                choice = int(input("Choose your option:\n1.check your timeline \n2.someone else time line:"))
                if choice == 2:
                    print("You chose to see someone else's timeline")
                    self.name = input("Enter the user's name")
                elif choice == 1:
                    print("You chose to see your timeline")
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

    def Friends(self):







