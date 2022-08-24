with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        if row[0]=="John":
            row[1]="Civil"
        print(f"{row[0]},is in {row[1]}")

