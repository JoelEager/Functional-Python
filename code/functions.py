"""
First-class functions in Python.

More information:
    https://en.wikipedia.org/wiki/First-class_function
    https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function
"""


def increment(value):
    return value + 1


def decrement(value):
    return value - 1


def decrement_more(value):
    return value - 10


def apply_function(funct, value, iterations):
    """
    Example of a function that takes another function as an argument
    """
    for index in range(iterations):
        value = funct(value)

    return value


def replace_decrement():
    """
    Replaces the decrement function with the decrement_more function
    """
    global decrement
    decrement = decrement_more

    # Keep in mind that this is bad practice and only done here to show how functions are really just references
    #   like everything else in Python


def run_demo():
    # See how function can be passed as arguments
    print("Increment:", apply_function(increment, 0, 10))
    print("Decrement:", apply_function(decrement, 0, 10))

    # In fact, function references can be overwritten like any other Python variable
    replace_decrement()
    print("Decrement again:", apply_function(decrement, 0, 10))


if __name__ == "__main__":
    run_demo()
