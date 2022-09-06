# Week 6:
It is a set of programs to showcase Unit test in Python

# Lines of Code
One way to measure the complexity of a program is to count its number of lines of code (LOC), excluding blank lines and comments. For instance, a program like

    # Say hello

    name = input("What's your name? ")
    print(f"hello, {name}")

has just two lines of code, not four, since its first line is a comment, and its second line is blank (i.e., just whitespace). That’s not that many, so odds are the program isn’t that complex. Of course, just because a program (or even function) has more lines of code than another doesn’t necessarily mean it’s more complex. For instance, a function like

    def is_even(n):
        if n % 2 == 0:
            return True
        else:
            return False

isn’t really twice as complex as a function like

    def is_even(n):
        return n % 2 == 0

even though the former has (more than) twice as many lines of code. In fact, the former might arguably be simpler if it’s easier to read! So lines of code should be taken with a grain of salt.

Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

## How to Test :

Here’s how to test the code manually:

Run the program with python lines.py. the program should exit with sys.exit and provide an error message:

    Too few command-line arguments

Create two python programs, hello.py and goodbye.py. Run python lines.py hello.py goodbye.py. the program should exit with sys.exit and provide an error message:

    Too many command-line arguments

Create a text file called invalid_extension.txt. Run the program with python lines.py invalid_extension.txt. the program should exit with sys.exit and provide an error message:

    Not a Python file

Run the program with python lines.py non_existent_file.py. Assuming non_existent_file.py doesn’t exist, the program should exit with sys.exit and provide an error message:

    File does not exist


# Back to the Bank
Perhaps the most popular place for Pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, sicilian.csv, below:

    Sicilian Pizza,Small,Large
    Cheese,$25.50,$39.95
    1 item,$27.50,$41.95
    2 items,$29.50,$43.95
    3 items,$31.50,$45.95
    Special,$33.50,$47.95

See regular.csv for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as ASCII art, like this one:

    +------------------+---------+---------+
    | Sicilian Pizza   | Small   | Large   |
    +==================+=========+=========+
    | Cheese           | $25.50  | $39.95  |
    +------------------+---------+---------+
    | 1 item           | $27.50  | $41.95  |
    +------------------+---------+---------+
    | 2 items          | $29.50  | $43.95  |
    +------------------+---------+---------+
    | 3 items          | $31.50  | $45.95  |
    +------------------+---------+---------+
    | Special          | $33.50  | $47.95  |
    +------------------+---------+---------+

In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.


## How to Test :
Here’s how to test the code manually:

Run the program with python pizza.py. the program should exit using sys.exit and provide an error message:

    Too few command-line arguments

Be sure to download regular.csv and sicilian.csv, placing them in the same folder as pizza.py. Run the program with python pizza.py regular.csv sicilian.csv. the program should output:

    Too many command-line arguments

Run the program with python pizza.py invalid_file.csv. Assuming invalid_file.csv doesn’t exist, the program should exit using sys.exit and provide an error message:

    File does not exist

Create a file named sicilian.txt. Run the program with python pizza.py sicilian.txt. the program should exit using sys.exit and provide an error message:

    Not a CSV file

Run the program with python pizza.py regular.csv. Assuming you’ve downloaded regular.csv, the program should print a table like the below:

    +-----------------+---------+---------+
    | Regular Pizza   | Small   | Large   |
    +=================+=========+=========+
    | Cheese          | $13.50  | $18.95  |
    +-----------------+---------+---------+
    | 1 topping       | $14.75  | $20.95  |
    +-----------------+---------+---------+
    | 2 toppings      | $15.95  | $22.95  |
    +-----------------+---------+---------+
    | 3 toppings      | $16.95  | $24.95  |
    +-----------------+---------+---------+
    | Special         | $18.50  | $26.95  |
    +-----------------+---------+---------+



# Re-requesting a Vanity Plate


    “Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in. That could do with a bit of cleaning, too.” She pointed her wand at Hedwig’s cage. “Scourgify.” A few feathers and droppings vanished.

    — Harry Potter and the Order of the Phoenix

Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format. Consider, for instance, this CSV file of students, before.csv, below:

    name,house
    "Abbott, Hannah",Hufflepuff
    "Bell, Katie",Gryffindor
    "Bones, Susan",Hufflepuff
    "Boot, Terry",Ravenclaw
    "Brown, Lavender",Gryffindor
    "Bulstrode, Millicent",Slytherin
    "Chang, Cho",Ravenclaw
    "Clearwater, Penelope",Ravenclaw
    "Crabbe, Vincent",Slytherin
    "Creevey, Colin",Gryffindor
    "Creevey, Dennis",Gryffindor
    "Diggory, Cedric",Hufflepuff
    "Edgecombe, Marietta",Ravenclaw
    "Finch-Fletchley, Justin",Hufflepuff
    "Finnigan, Seamus",Gryffindor
    "Goldstein, Anthony",Ravenclaw
    "Goyle, Gregory",Slytherin
    "Granger, Hermione",Gryffindor
    "Johnson, Angelina",Gryffindor
    "Jordan, Lee",Gryffindor
    "Longbottom, Neville",Gryffindor
    "Lovegood, Luna",Ravenclaw
    "Lupin, Remus",Gryffindor
    "Malfoy, Draco",Slytherin
    "Malfoy, Scorpius",Slytherin
    "Macmillan, Ernie",Hufflepuff
    "McGonagall, Minerva",Gryffindor
    "Midgen, Eloise",Gryffindor
    "McLaggen, Cormac",Gryffindor
    "Montague, Graham",Slytherin
    "Nott, Theodore",Slytherin
    "Parkinson, Pansy",Slytherin
    "Patil, Padma",Gryffindor
    "Patil, Parvati",Gryffindor
    "Potter, Harry",Gryffindor
    "Riddle, Tom",Slytherin
    "Robins, Demelza",Gryffindor
    "Scamander, Newt",Hufflepuff
    "Slughorn, Horace",Slytherin
    "Smith, Zacharias",Hufflepuff
    "Snape, Severus",Slytherin
    "Spinnet, Alicia",Gryffindor
    "Sprout, Pomona",Hufflepuff
    "Thomas, Dean",Gryffindor
    "Vane, Romilda",Gryffindor
    "Warren, Myrtle",Ravenclaw
    "Weasley, Fred",Gryffindor
    "Weasley, George",Gryffindor
    "Weasley, Ginny",Gryffindor
    "Weasley, Percy",Gryffindor
    "Weasley, Ron",Gryffindor
    "Wood, Oliver",Gryffindor
    "Zabini, Blaise",Slytherin

Source: en.wikipedia.org/wiki/List_of_Harry_Potter_characters

Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:

    Dear Potter, Harry,

Rather than with, for instance:

    Dear Harry,

In a file called scourgify.py, implement a program that:

- Expects the user to provide two command-line arguments:
    - the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
    - the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
- Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
## How to Test :
Here’s how to test the code manually:

Run the program with python scourgify.py. the program should exit using sys.exit and provide an error message:

    Too few command-line arguments

Create empty files 1.csv, 2.csv, and 3.csv. Run the program with python scourgify.py 1.csv 2.csv 3.csv. the program should output:

    Too many command-line arguments

Run the program with python scourgify.py invalid_file.csv output.csv. Assuming invalid_file.csv doesn’t exist, the program should exit using sys.exit and provide an error message:

    Could not read invalid_file.csv

Run the program with python scourgify.py before.csv after.csv. Assuming before.csv exists, the program should create a new file, after.csv, whose columns should be, in order, first, last, and house.


# CS50 P-Shirt
In a file called shirt.py, implement a program that expects exactly two command-line arguments:

- in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
- in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

- if the user does not specify exactly two command-line arguments,
- if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
- if the input’s name does not have the same extension as the output’s name, or
- if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
## How to Test :
Here’s how to test the code manually:

Run your program with python shirt.py. Your program should exit using sys.exit and provide an error message:

    Too few command-line arguments   

Be sure to download images.and run your program with python shirt.py before1.jpg before2.jpg before3.jpg. Your program should output:

    Too many command-line arguments

Run your program with python shirt.py before1.jpg invalid_format.bmp. Your program should exit using sys.exit and provide an error message:

    Invalid output

Run your program with python shirt.py before1.jpg after1.png. Your program should exit using sys.exit and provide an error message:

    Input and output have different extensions

Run your program with python shirt.py non_existent_image.jpg after1.jpg. Your program should exit using sys.exit and provide an error message:

    Input does not exist

Run your program with python shirt.py before1.jpg after1.jpg
