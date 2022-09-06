
# Week 0

Set of Program to showcase Functions in Python

# IndoorVoice :
WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, is a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.


## How to Test :
Here’s how to test the code. At the indoor/ $ prompt in your terminal :

Run the program with python indoor.py. Type HELLO and press Enter, the program should output 

    hello
Run the program with python indoor.py. Type THIS IS CS50 and press Enter, the program should output 

    this is cs50
Run the program with python indoor.py. Type 50 and press Enter, the program should output 

    50

# Playback Speed :
Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, is a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

## How to Test :
Here’s how to test code:

Run the program with python playback.py. Type This is CS50 and press Enter, the program should output:

    This...is...CS50    

Run the program with python playback.py. Type This is our week on functions and press Enter, the program should output:

    This...is...our...week...on...functions

Run the program with python playback.py. Type Let's implement a function called hello and press Enter, the program should output

    Let's...implement...a...function...called...hello

# Making Faces :
Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, is a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, is a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.


## How to Test :
Here’s how to test code manually:

Run the program with python faces.py. Type Hello :) and press Enter, the program should output:

    Hello 🙂

Run the program with python faces.py. Type Goodbye :( and press Enter, the program should output:

    Goodbye 🙁

Run the program with python faces.py. Type Hello :) Goodbye :( and press Enter, the program should output

    Hello 🙂 Goodbye 🙁

# Einstein :
we all have heard of E = mc^2 that , wherein E represents energy (measured in Joules), m represents mass (measured in kilograms), and c
represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, is a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

## How to Test :
Here’s how to test your code manually:

Run the program with python einstein.py. Type 1 and press Enter the program should output:

    90000000000000000

Run the program with python einstein.py. Type 14 and press Enter the program should output:

    1260000000000000000

Run the program with python einstein.py. Type 50 and press Enter the program should output

    4500000000000000000

# Tip Calculator :
In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost, the main function for tip calculator, below!

    def main():
        dollars = dollars_to_float(input("How much was the meal? "))
        percent = percent_to_float(input("What percentage would you like to tip? "))
        tip = dollars * percent
        print(f"Leave ${tip:.2f}")


    def dollars_to_float(d):
        # TODO


    def percent_to_float(p):
        # TODO


    main()


Implement two functions:

    dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
    percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.

Assume that the user will input values in the expected formats.

## How to Test :
Here’s how to test code manually:

Run the program with python tip.py. Type $50.00 and press Enter. Then, type 15% and press Enter,the program should output:

    Leave $7.50    

Run the program with python tip.py. Type $100.00 and press Enter. Then, type 18% and press Enter, the program should output:

    Leave $18.00

Run the program with python tip.py. Type $15.00 and press Enter. Then, type 25% and press Enter, the program should output

    Leave $3.75

