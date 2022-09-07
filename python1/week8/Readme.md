# Week 8:
It is a set of programs to showcase Object-Oriented programming  in Python

# Seasons of Love
Assuming there are 365 days in a year, there are 365 * 24 * 60 =525,600 minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour). But how many minutes are there in two or more years? Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar, as some of them could have 1 * 24 * 60 = 1,440

additional minutes. In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap years there have been since! There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead. Fortunately, Python comes with a datetime module that has a class called date that can help, per docs.python.org/3/library/datetime.html#date-objects.

In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also with one or more other functions as well:

    from datetime import date


    def main():
        ...


    ...


    if __name__ == "__main__":
        main()


## Libraries to install :
- Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:

        pip install inflect



## How to Test :

Here’s how to test the code manually:


- Run your program with python seasons.py. Ensure your program prompts you for a birthdate. Type a date one year ago from today, in the specified format, then press Enter. Your program should sing print 
    
         Five hundred twenty-five thousand, six hundred minutes.

- Run your program with python seasons.py. Type a date two years ago from today, in the specified format, then press Enter. Your program should print 
        
        One million, fifty-one thousand, two hundred minutes.

- Run your program with python seasons.py. Type a date of your choice, but this time use an invalid format. Press Enter and your program should exit using sys.exit without raising an Exception.

# Felipe’s Taqueria:
Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:

- __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

- __str__ should return a str with 🍪, where is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
- deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
- withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
- capacity should return the cookie jar’s capacity.
- size should return the number of cookies actually in the cookie jar.

Structure your class per the below. You may not alter these methods’ parameters, but you may add your own methods.

    class Jar:
        def __init__(self, capacity=12):
            ...

        def __str__(self):
            ...

        def deposit(self, n):
            ...

        def withdraw(self, n):
            ...

        @property
        def capacity(self):
            ...

        @property
        def size(self):
            ...


Either before or after you implement jar.py, additionally implement, in a file called test_jar.py, four or more functions that collectively test your implementation of Jar thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

    pytest test_jar.py

Note that it’s not as easy to test instance methods as it is to test functions alone, since instance methods sometimes manipulate the same “state” (i.e., instance variables). To test one method (e.g., withdraw), then, you might need to call another method first (e.g., deposit). But the method you call first might itself not be correct!

Structure your test_jar.py per the belowx`

    from jar import Jar


    def test_init():
        ...


    def test_str():
        jar = Jar()
        assert str(jar) == ""
        jar.deposit(1)
        assert str(jar) == "🍪"
        jar.deposit(11)
        assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


    def test_deposit():
        ...


    def test_withdraw():
        ...


## How to Test :
Here’s how to test the code manually:


- Open your test_jar.py file and import your Jar class with from jar import Jar. Create a function called test_init, wherein you create a new instance of Jar with jar = Jar(). assert that this jar has the capacity it should, then run your tests with pytest test_jar.py.
- Add another function to your test_jar.py file called test_str. In test_str, create a new instance of your Jar class and deposit a few cookies. assert that str(jar) prints out as many cookies as have been deposited, then run your tests with pytest test_jar.py.
- Add another function to your test_jar.py file called test_deposit. In test_deposit, create a new instance of your Jar class and deposit a few cookies. assert that the jar’s size attribute is as large as the number of cookies that have been deposited. Also assert that, if you deposit more than the jar’s capacity, deposit should raise a ValueError. Run your tests with pytest test_jar.py.
- Add another function to your test_jar.py file called test_withdraw. In test_withdraw, create a new instance of your Jar class and first deposit a few cookies. assert that withdrawing from the jar leaves the appropriate number of cookies in the jar’s size attribute. Also assert that, if you withdraw more than the jar’s size, withdraw should raise a ValueError. Run your tests with pytest test_jar.py.
# CS50 Shirtificate

Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

- The orientation of the PDF should be Portrait.
- The format of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should “CS50 Shirtificate” as text, centered horizontally.
- The shirt’s image should be centered horizontally.
- The user’s name should be on top of the shirt, in white text.

All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.

## How to Test :
Here’s how to test the code manually:

- Run your program with shirtificate.py. Make sure your program prompts you for a name. Enter your own name and press Enter. Your program should create a file, shirtificate.pdf, containing the name you entered as input overlaid on a rendering of shirtificate.png.
