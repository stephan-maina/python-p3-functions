# lib/functions.py

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print("Hello, {}!".format(name))

def greet_with_default(name="programmer"):
    print("Hello, {}!".format(name))

def add(num1, num2):
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2

# Testing the methods
if __name__ == "__main__":
    greet_programmer()
    greet("Stephan Maina")
    greet_with_default("Bat-Tziyon Mbiki")
    greet_with_default()
    result = add(10, 5)
    print("The sum is:", result)
    halved_value = halve(20)
    print("Half of 20 is:", halved_value)
    invalid_result = halve("two")
    print("Invalid result:", invalid_result)
