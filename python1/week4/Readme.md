
# Week 4:
it is a set of programs to showcase Libraries in Python

# Emojize
Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍. Some programs additionally support aliases, whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.

See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.

Emojize.py, is a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

## Libraries to install:


Note that the emoji module comes with two functions, per pypi.org/project/emoji, one of which is emojize, which takes an optional, named parameter called language. You can install it with:

    pip install emoji



## How to Test :

Here’s how to test the code manually:


Run the program with python Emojize.py. Type :1st_place_medal: and press Enter. the program should output:

    Output: 🥇

Run the program with python Emojize.py. Type :money_bag: and press Enter. the program should output:

    Output: 💰

Run the program with python Emojize.py. Type :smile_cat: and press Enter. the program should output:

    Output: 😸

# Frank, Ian and Glen’s Letters
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

    _ _ _          _   _     _
    | (_) | _____  | |_| |__ (_)___
    | | | |/ / _ \ | __| '_ \| / __|
    | | |   <  __/ | |_| | | | \__ \
    |_|_|_|\_\___|  \__|_| |_|_|___/

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called Figlet.py, implement a program that:

- Expects zero or two command-line arguments:
   - Zero if the user would like to output text in a random font.
   - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
## Libraries to install:
You can install pyfiglet with:

    pip install pyfiglet


## How to Test :
Here’s how to test the code manually:


Run the program with python Figlet.py test. the program should exit via sys.exit and print an error message:

Invalid usage

Run the program with python Figlet.py -a slant. the program should exit via sys.exit and print an error message:

Invalid usage

Run the program with python Figlet.py -f invalid_font. the program should exit via sys.exit and print an error message:

Invalid usage

Run the program with python Figlet.py -f slant. Type CS50. the program should print the following:

       ___________ __________ 
      / ____/ ___// ____/ __ \
     / /    \__ \/___ \/ / / /
    / /___ ___/ /___/ / /_/ / 
    \____//____/_____/\____/  

Run the program with python Figlet.py -f rectangles. Type Hello, world. the program should print the following:

     _____     _ _                        _   _ 
    |  |  |___| | |___      _ _ _ ___ ___| |_| |
    |     | -_| | | . |_   | | | | . |  _| | . |
    |__|__|___|_|_|___| |  |_____|___|_| |_|___|
                      |_|                       

Run the program with python Figlet.py -f alphabet. Type Moo. the program should print the following:

    M   M         
    MM MM         
    M M M ooo ooo 
    M   M o o o o 
    M   M ooo ooo                     


# Adieu, Adieu
In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

    Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

    Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

Adieu.py, is a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and
names with commas and one and, as in the below:

    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

## Libraries to install:

    pip install inflect

## How to Test :
Here’s how to test the code manually:

Run the program with python Adieu.py. Type Liesl and press Enter, followed by control-d. the program should output:

    Adieu, adieu, to Liesl 

Run the program with python Adieu.py. Type Liesl and press Enter, then type Friedrich and press Enter, followed by control-d. the program should output:

    Adieu, adieu, to Liesl and Friedrich

Run the program with python Adieu.py. Type Liesl and press Enter, then type Friedrich and press Enter. Now type Louisa and press Enter, followed by control-d. the program should output:

    Adieu, adieu, to Liesl, Friedrich, and Louisa



# Guessing Game
Game.py, is a program that:

- Prompts the user for a level, 
- If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and n inclusive, using the random module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

    - If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    - If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    - If the guess is the same as that integer, the program should output Just right! and exit.


## How to Test :
Here’s how to test code manually:


Run the program with python Game.py. Type cat at a prompt that says Level: and press Enter. the program should reprompt you:

    Level:   

Run the program with python Game.py. Type -1 at a prompt that says Level: and press Enter. the program should reprompt you:

    Level:   

Run the program with python Game.py. Type 10 at a prompt that says Level: and press Enter. the program should now be ready to accept guesses:

    Guess:   

Run the program with python Game.py. Type 10 at a prompt that says Level: and press Enter. Then type cat. the program should reprompt you:

    Guess:   

Run the program with python Game.py. Type 10 at a prompt that says Level: and press Enter. Then type -1. the program should reprompt you:

    Guess:   

Run the program with python Game.py. Type 1 at a prompt that says Level: and press Enter. Then type 1. the program should output:

    Just right!  

There’s only one possible number the answer could be!
Run the program with python Game.py. Type 10 at a prompt that says Level: and press Enter. Then type 100. the program should output:

    Too large!  

Looks like you’re guessing outside the range you specified.
Run the program with python Game.py. Type 10000 at a prompt that says Level: and press Enter. Then type 1. the program should output:

    Too small!  

# Little Professor
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

Professor.py, implement a program that:

- Prompts the user for a level,If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).
- Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the user’s score, a number out of 10.
## How to Test :
Here’s how to test the code manually:

Run your program with python Professor.py. Type -1 and press Enter. Your program should reprompt you:

    Level:   

Run your program with python Professor.py. Type 4 and press Enter. Your program should reprompt you:

    Level:   

Run your program with python Professor.py. Type 1 and press Enter. Your program should begin posing addition problems with positive, single-digit integers. For example:

    6 + 6 =    

Your program should output 10 distinct problems before printing the number of questions you answered correctly and exiting.
Run your program with python Professor.py. Type 1 and press Enter. Answer the first question incorrectly. Your program should output:

    EEE

before reprompting you with the same question.
Run your program with python Professor.py. Type 1 and press Enter. Answer the first question incorrectly, three times. Your program should output the correct answer. For example:

    6 + 6 = 12

and then move on to another question. Answer the remaining questions correctly. Your program should output a score of 9.

Run your program with python Professor.py. Type 1 and press Enter. Answer all 10 questions correctly. Your program should output a score of 10.

# Bitcoin Price Index
Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called Bitcoin.py, implement a program that:
- Expects the user to specify as a command-line argument the number of Bitcoins,n , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
- Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

    import requests

    try:
        ...
    except requests.RequestException:
        ...

- Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.

## Libraries to install:
Note that the requests module comes with quite a few methods, per requests.readthedocs.io/en/latest, among which are get, per requests.readthedocs.io/en/latest/user/quickstart/#make-a-request, and json, per requests.readthedocs.io/en/latest/user/quickstart/#json-response-content. You can install it with:

    pip install requests

## How to Test :
Here’s how to test the code manually:

Run your program with python Bitcoin.py. Your program should use sys.exit to exit with an error message:

    Missing command-line argument   

Run your program with python Bitcoin.py cat. Your program should use sys.exit to exit with an error message:

    Command-line argument is not a number

Run your program with python Bitcoin.py 1. Your program should output the price of a single Bitcoin to four decimal places, using , as a thousands separator.

Run your program with python Bitcoin.py 2. Your program should output the price of two Bitcoin to four decimal places, using , as a thousands separator.

Run your program with python Bitcoin.py 2.5. Your program should output the price of 2.5 Bitcoin to four decimal places, using , as a thousands separator.
