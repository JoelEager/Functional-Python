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
    for index in range(iterations):
        value = funct(value)

    return value


if __name__ == "__main__":
    # See how function can be passed as arguments
    print("Increment:", apply_function(increment, 0, 10))
    print("Decrement:", apply_function(decrement, 0, 10))

    # In fact, function references behave like any other Python variable
    decrement = decrement_more
    print("Decrement again:", apply_function(decrement, 0, 10))
