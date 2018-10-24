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


def apply_function(funct, value, iterations):
    for index in range(iterations):
        value = funct(value)

    return value


if __name__ == "__main__":
    print("Increment:", apply_function(increment, 0, 10))
    print("Decrement:", apply_function(decrement, 0, 10))
