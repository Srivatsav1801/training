
# Week 2:
It is a set of programs to showcase Loops in Python

# camelCase 

In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

camel.py,is a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
## How to Test :

Here’s how to test the code manually:

Run the program with python camel.py. Type name and press Enter, the program should output:

    name   

Run the program with python camel.py. Type firstName and press Enter, the program should output:

    first_name

Run the program with python camel.py. Type preferredFirstName and press Enter, the program should output

    preferred_first_name



# Coke Machine 
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

coke.py, is a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
## How to Test :
Here’s how to test the code manually:

Run the program with python coke.py. Type 25 and press Enter, the program should output:

    Amount due: 25   

and continue prompting the user for coins.
Run the program with python coke.py. Type 10 and press Enter, the program should output:

    Amount due: 40

and continue prompting the user for coins.
Run the program with python coke.py. Type 5 and press Enter, the program should output:

    Amount due: 45

and continue prompting the user for coins.
Run the program with python coke.py. Type 30 and press Enter, the program should output:

    Amount due: 50

and continue prompting the user for coins.
Run the program with python coke.py. Type 25 and press Enter, then type 25 again and press Enter, the program should halt and display:

    Change owed: 0

Run the program with python coke.py. Type 25 and press Enter, then type 10 and press Enter, Type 25 again and press Enter, after which the program should halt and display:

    Change owed: 10



# Just setting up my twttr 
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. twttr.py, is a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
## How to Test :
Here’s how to test the code manually:

Run the program with python twttr.py. Type Twitter and press Enter, the program should output:

    Twttr   

Run the program with python twttr.py. Type What's the name? and press Enter, the program should output:

    Wht's yr nm?

Run the program with python twttr.py. Type CS50 and press Enter, the program should output

    CS50

# Vanity Plates
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure the program, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
## How to Test :
Here’s how to test code manually:


Run the program with python plates.py. Type CS50 and press Enter, the program should output:

    Valid

Run the program with python plates.py. Type CS05 and press Enter, the program should output:

    Invalid

Run the program with python plates.py. Type CS50P and press Enter, the program should output

    Invalid

Run the program with python plates.py. Type PI3.14 and press Enter, the program should output

    Invalid

Run the program with python plates.py. Type H and press Enter, the program should output

    Invalid

Run the program with python plates.py. Type OUTATIME and press Enter, the program should output

    Invalid




# Nutrition Facts
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

## How to Test :
Here’s how to test the code manually:

Run the program with python nutrition.py. Type Apple and press Enter, the program should output:

    Calories: 130   

Run the program with python nutrition.py. Type Avocado and press Enter, the program should output:

    Calories: 50

Run the program with python nutrition.py. Type Sweet Cherries and press Enter, the program should output

    Calories: 100

Run the program with python nutrition.py. Type Tomato and press Enter, the program should output nothing.
