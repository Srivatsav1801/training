# Week 7:
It is a set of programs to showcase Regular expressions in Python

# NUMB3RS
An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

    import re
    import sys


    def main():
        print(validate(input("IPv4 Address: ")))


    def validate(ip):
        ...


    ...


    if __name__ == "__main__":
        main()

## How to Test :

Here’s how to test the code manually:

- Run your program with python numb3rs.py. Ensure your program prompts you for an IPv4 address. Type 127.0.0.1, followed by Enter. Your validate function should return True.

- Run your program with python numb3rs.py. Type 255.255.255.255, followed by Enter. Your validate function should return True.
    
- Run your program with python numb3rs.py. Type 512.512.512.512, followed by Enter. Your validate function should return False.
    
- Run your program with python numb3rs.py. Type 1.2.3.1000, followed by Enter. Your validate function should return False.

- Run your program with python numb3rs.py. Type cat, followed by Enter. Your validate function should return False.


# Watch on YouTube
It turns out that (most) YouTube videos can be embedded in other websites, just like the above. For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a laptop or desktop, click Share, and then click Embed, you’ll see HTML (the language in which web pages are written) like the below, which you could then copy into your own website’s source code, wherein iframe is an HTML “element,” and src is one of several HTML “attributes” therein, the value of which, between quotes, is https://www.youtube.com/embed/xvFZjo5PgG0.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Because some HTML attributes are optional, you could instead minimally embed just the below.

    <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages (e.g., https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter, shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.

In a file called watch.py, implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.

    http://youtube.com/embed/xvFZjo5PgG0
    https://youtube.com/embed/xvFZjo5PgG0
    https://www.youtube.com/embed/xvFZjo5PgG0

Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

    import re


    def main():
        print(parse(input("HTML: ")))


    def parse(s):
        ...


    ...


    if __name__ == "__main__":
        main()


## How to Test :
Here’s how to test the code manually:


- Run the program with python watch.py. Ensure the program prompts you for HTML, then copy/paste the below:

      <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

     Press enter and the program should output https://youtu.be/xvFZjo5PgG0. Notice how, though the src attribute is prefixed with http://www.youtube.com/embed/, the resulting link is prefixed with https://youtu.be/.

- Run the program with python watch.py. Ensure the program prompts you for HTML, then copy/paste the below:

         <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    Press enter and the program should still output https://youtu.be/xvFZjo5PgG0.

- Run the program with python watch.py. Ensure the program prompts you for HTML, then copy/paste the below:

         <iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>

    Press enter and the program should output None. Notice how the src attribute doesn’t point to a YouTube link!



# Working 9 to 5

Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

- 9:00 AM to 5:00 PM
- 9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

    import re
    import sys


    def main():
        print(convert(input("Hours: ")))


    def convert(s):
        ...


    ...


    if __name__ == "__main__":
        main()

## How to Test :
Here’s how to test the code manually:


- Run your program with python working.py. Ensure your program prompts you for a time. Type 9 AM to 5 PM, followed by Enter. Your program should output 
    
    09:00 to 17:00.
- Run your program with python working.py. Type 9:00 AM to 5:00 PM, followed by Enter. Your program should again output 
    
    09:00 to 17:00.
- Run your program with python working.py. Ensure your program prompts you for a time. Type 10 PM to 8 AM, followed by Enter. Your program should output 
    
    22:00 to 08:00.
- Run your program with python working.py. Ensure your program prompts you for a time. Type 10:30 PM to 8:50 AM, followed by Enter. Your program should again output 
    
    22:30 to 08:50.
- Run your program with python working.py. Ensure your program prompts you for a time. Try intentionally inducing a ValueError by typing 9:60 AM to 5:60 PM, followed by Enter. Your program should indeed raise a ValueError.
- Run your program with python working.py. Ensure your program prompts you for a time. Try intentionally inducing a ValueError by typing 9 AM - 5 PM, followed by Enter. Your program should indeed raise a ValueError.
- Run your program with python working.py. Ensure your program prompts you for a time. Try intentionally inducing a ValueError by typing 09:00 AM - 17:00 PM, followed by Enter. Your program should indeed raise a ValueError.


# Regular, um, Expressions
It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The more you do it, though, the more noticeable it tends to be!

In a file called um.py, implement a function called count that expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. For instance, given text like hello, um, world, the function should return 1. Given text like yummy, though, the function should return 0.

Structure um.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

    import re
    import sys


    def main():
        print(count(input("Text: ")))


    def count(s):
        ...


    ...


    if __name__ == "__main__":
        main()


## How to Test :
Here’s how to test the code manually:


- Run your program with python um.py. Ensure your program prompts you for an input. Type um, followed by Enter. Your count function should return 1.
- Run your program with python um.py. Type um?, followed by Enter. Your count function should return 1.
- Run your program with python um.py. Type Um, thanks for the album., followed by Enter. Your count function should return 1.
- Run your program with python um.py. Type Um, thanks, um..., followed by Enter. Your count function should return 2.

# Response Validation
In a file called response.py, using either validator-collection or validators from PyPI, implement a program that prompts the user for an email address via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address. You may not use re. And do not validate whether the email address’s domain name actually exists.

## libraries to install:

Install validator-collection with:

    pip install validator-collection

## How to Test :

Here’s how to test The code manually:

- Run the program with python response.py. Ensure the program prompts you for an email, then type malan@harvard.edu, followed by Enter. Your program should output 
    
        Valid
- Run the program with python response.py. Type the own email, followed by Enter. Your program should output
        
        Valid
- Run the program with python response.py. Type malan@@@harvard.edu, followed by Enter. Your program should output 
        
        Invalid
- Run the program with python response.py. Mistype the own email, including an extra . before .com, for example. Press enter and your program should output 
        
        Invalid
