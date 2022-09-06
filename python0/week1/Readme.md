
# Week 1:
it is a set of programs to showcase Conditions in Python

# Deep Thought

    “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
    “You’re really not going to like it,” observed Deep Thought.
    “Tell us!”
    “All right,” said Deep Thought. “The Answer to the Great Question…”
    “Yes…!”
    “Of Life, the Universe and Everything…” said Deep Thought.
    “Yes…!”
    “Is…” said Deep Thought, and paused.
    “Yes…!”
    “Is…”
    “Yes…!!!…?”
    “Forty-two,” said Deep Thought, with infinite majesty and calm.”

    — The Hitchhiker’s Guide to the Galaxy, Douglas Adams

deep.py, is a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
Here’s how to test your code manually:

## How to Test :

Run the program with python deep.py. Type 42 and press Enter, the program should output:

    Yes 

Run the program with python deep.py. Type Forty Two and press Enter, the program should output:

    Yes

Run the program with python deep.py. Type forty-two and press Enter, the program should output

    Yes

Run the program with python deep.py. Type 50 and press Enter, the program should output

    No

# Home Federal Savings Bank:
In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
## How to Test :
Here’s how to test  code manually:

Run the program with python bank.py. Type Hello and press Enter, the program should output:

    $0 

Run the program with python bank.py. Type Hello, Newman and press Enter, the program should output:

    $0

Run the program with python bank.py. Type How you doing? and press Enter, the program should output

    $20

Run the program with python bank.py. Type What's happening? and press Enter, the program should output

    $100


# File Extensions :
Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg
 
extensions.py, is a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
## How to Test :
Here’s how to test code manually:

Run the program with python extensions.py. Type happy.jpg and press Enter, the program should output:

    image/jpeg   

Run the program with python extensions.py. Type document.pdf and press Enter, the program should output:

    application/pdf



# Math Interpreter
Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

interpreter.py, is a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

    x is an integer
    y is +, -, *, or /
    z is an integer

For instance, if the user inputs 1 + 1, program should output 2.0. Assume that, if y is /, then z will not be 0.
## How to Test :
Here’s how to test code manually:

Run the program with python interpreter.py. Type 1 + 1 and press Enter, the program should output:

    2.0 

Run the program with python interpreter.py. Type 2 - 3 and press Enter, the program should output:

    -1.0

Run the program with python interpreter.py. Type 2 * 2 and press Enter, the program should output

    4.0

Run the program with python interpreter.py. Type 50 / 5 and press Enter, the program should output

    10.0



# Meal Time :
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, is a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure the program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
    
    def main():
        ...


    def convert(time):
        ...


    if __name__ == "__main__":
        main()

## How to Test :
Here’s how to test the code manually:

Run the program with python meal.py. Type 7:00 and press Enter, the program should output:

    breakfast time   

Run the program with python meal.py. Type 7:30 and press Enter, the program should output:

    breakfast time

Run the program with python meal.py. Type 12:42 and press Enter, the program should output

    lunch time

Run the program with python meal.py. Type 18:32 and press Enter, the program should output

    dinner time

Run the program with python meal.py. Type 11:11 and press Enter, the program should output nothing.
