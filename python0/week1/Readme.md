
1.deep.py, is a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
<br/>
<br />2.bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively
<br/>
<br/>3.extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
<br/>
<br/>.gif
<br/>.jpg
<br/>.jpeg
<br/>.png
<br/>.pdf
<br/>.txt
<br/>.zip
<br/>If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
<br/>
<br/>4.interpreter.py is a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
<br/>x is an integer
<br/>y is +, -, *, or /
<br/>z is an integer
<br/>For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0
<br/>
<br/>5.meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
