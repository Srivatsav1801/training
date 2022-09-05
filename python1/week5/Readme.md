
# Week 4:
it is a set of programs to showcase Unit test in Python

# Testing my twttr
In a file called Twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

    def main():
        ...


    def shorten(word):
        ...


    if __name__ == "__main__":
        main()

Then, in a file called Test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest Test_twttr.py

## How to Test :

o test your tests, run pytest test_twttr.py. Try to use correct and incorrect versions of twttr.py to determine how well your tests spot errors:

- Ensure you have a correct version of twttr.py. Run your tests by executing pytest test_twttr.py. pytest should show that all of your tests have passed.
- Modify the correct version of twttr.py in such a way as to create a bug. Your program might, for example, mistakenly only omit lowercase vowels! Run your tests by executing pytest test_twttr.py. pytest should show that at least one of your tests has failed.



# Back to the Bank
In a file called Bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. Only main should call print.

    def main():
        ...


    def value(greeting):
        ...


    if __name__ == "__main__":
        main()

Then, in a file called Test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest Test_bank.py

## How to Test :
To test your tests, run pytest Test_bank.py. Try to use correct and incorrect versions of bank.py to determine how well your tests spot errors:

- Ensure you have a correct version of Bank.py. Run your tests by executing pytest Test_bank.py. pytest should show that all of your tests have passed.
- Modify the correct version of Bank.py, changing the values provided for each greeting. Your program might, for example, mistakenly provide $100 to a customer greeted by “Hello” and $0 to a customer greeted with “What’s up”! Now, run your tests by executing pytest Test_bank.py. pytest should show that at least one of your tests has failed.


# Re-requesting a Vanity Plate
In a file called Plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

    def main():
        ...


    def is_valid(s):
        ...


    if __name__ == "__main__":
        main()

Then, in a file called Test_Plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest Test_plates.py

## How to Test :
To test your tests, run pytest test_plates.py. Try to use correct and incorrect versions of plates.py to determine how well your tests spot errors:

- Ensure you have a correct version of Plates.py. Run your tests by executing pytest Test_plates.py. pytest should show that all of your tests have passed.
- Modify the correct version of Plates.py, perhaps eliminating some of its constraints. Your program might, for example, mistakenly print “Valid” for a license plate of any length! Run your tests by executing pytest Test_plates.py. pytest should show that at least one of your tests has failed.


# Refueling
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

- convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
- gauge expects an int and returns a str that is:

    - "E" if that int is less than or equal to 1,
    - "F" if that int is greater than or equal to 99,
    - and "Z%" otherwise, wherein Z is that same int.

            def main():
                ...


            def convert(fraction):
                ...


            def gauge(percentage):
                ...


            if __name__ == "__main__":
                main()

Then, in a file called Test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest Test_fuel.py

## How to Test :
To test your tests, run pytest Test_fuel.py. Try to use correct and incorrect versions of fuel.py to determine how well your tests spot errors:

- Ensure you have a correct version of Fuel.py. Run your tests by executing pytest Test_fuel.py. pytest should show that all of your tests have passed.
- Modify the correct version of Fuel.py, changing the return values of convert. Your program might, for example, mistakenly return a str instead of an int. Run your tests by executing pytest Test_fuel.py. pytest should show that at least one of your tests has failed.
- Similarly, modify the correct version of Fuel.py, changing the return values of gauge. Your program might, for example, mistakenly omit a % in the resulting str. Run your tests by executing pytest Test_fuel.py. pytest should show that at least one of your tests has failed.

  
