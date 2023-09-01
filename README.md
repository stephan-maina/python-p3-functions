# Python Functions Testing

This is a Python project that includes a module functions.py with a set of functions and a test suite lib_test.py to test these functions.

# Project Structure

The project structure looks like this:

project-root/
│
├── lib/
│ ├── functions.py
│
├── testing/
│ ├── lib_test.py
lib/functions.py: Contains a set of functions to be tested.
testing/lib_test.py: Includes test cases to test the functions defined in functions.py.

# Functions

greet_programmer()
This function returns a greeting message for a programmer.

greet(name)
This function takes a name argument and returns a greeting message with the provided name.

greet_with_default(name="programmer")
This function takes an optional name argument (default is "programmer") and returns a greeting message with the provided name.

add(num1, num2)
This function takes two numbers as arguments and returns their sum.

halve(number)
This function takes a number as an argument and returns half of that number. If the input is not a number, it returns None.

# Running Tests

To run the tests and verify the functionality of the functions, execute the following command in your terminal:

python3 testing/lib_test.py
The tests will be run, and the results will be displayed in the terminal.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

## Conclusion

Python's function syntax has a few things that make them distinct from JavaScript
functions. In particular, make sure you pay attention to the **indentation**
**levels** of the code inside of Python functions, and always call functions with
the right number of arguments to avoid errors.

***

## Resources

- [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
