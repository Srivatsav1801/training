
# Week 3:
it is a set of programs to showcase Exceptions in Python

# Fuel Gauge
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

Fuel.py, is a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


## How to Test :

Here’s how to test the code manually:


Run the program with python fuel.py. Type 3/4 and press Enter. the program should output:

    75% 

Run the program with python fuel.py. Type 1/4 and press Enter. the program should output:

    25%

Run the program with python fuel.py. Type 4/4 and press Enter. the program should output:

    F

Run the program with python fuel.py. Type 0/4 and press Enter. the program should output:

    E

Run the program with python fuel.py. Type 4/0 and press Enter. the program should handle a ZeroDivisionError and prompt the user again.

Run the program with python fuel.py. Type three/four and press Enter. the program should handle a ValueError and prompt the user again.

Run the program with python fuel.py. Type 1.5/3 and press Enter. the program should handle a ValueError and prompt the user again.

Run the program with python fuel.py. Type 5/4 and press Enter. the program should prompt the user again.




# Felipe’s Taqueria:
One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

    {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
taqueria.py,is a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

## How to Test :
Here’s how to test the code manually:


Run the program with python taqueria.py. Type Taco and press Enter, then type Taco again and press Enter. the program should output:

    Total: $6.00  

and continue prompting the user until they input control-d.
Run the program with python taqueria.py. Type Baja Taco and press Enter, then type Tortilla Salad and press enter. the program should output:

    Total: $12.00

and continue prompting the user until they input control-d.
Run the program with python taqueria.py. Type Burger and press Enter. the program should reprompt the user.

# Grocery List
Suppose that you’re in the habit of making a list of items you need from the grocery store.

grocery.py, is a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
## How to Test :
Here’s how to test the code manually:

Run your program with python grocery.py. Type mango and press Enter, then type strawberry and press Enter, followed by control-d. Your program should output:

    1 MANGO
    1 STRAWBERRY

Run your program with python grocery.py. Type milk and press Enter, then type milk again and press Enter, followed by control-d. Your program should output:

    2 MILK

Run your program with python grocery.py. Type tortilla and press Enter, then type sweet potato and press Enter, followed by control-d. Your program should output:

    1 SWEET POTATO
    1 TORTILLA

