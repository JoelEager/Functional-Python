"""
An alternate use of iterators to populate Python data structures in a compact and readable way.
    (Comprehensions are basically syntactical sugar for map(), filter(), and constructors.)

Docs:
    List comprehensions: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    Set comprehensions: https://docs.python.org/3/tutorial/datastructures.html#sets
    Dictionary comprehensions: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
"""

from random import randint


def run_demo():
    print("Comprehensions are a concise way to create lists, sets, and dictionaries")
    a_list = [value for value in range(10)]
    a_set = {value for value in range(10)}
    a_dict = {value: value ** 2 for value in range(10)}
    # They're mostly just syntactical sugar around a constructor and a map() call

    print(a_list, a_set, a_dict, sep="\n")

    print("\nArbitrary expressions can go in the first part of the comprehension")
    print([index ** 2 for index in range(10)])

    print("\nYou can also add an 'if' clause to the end to filter the items")
    print([value for value in range(10) if value % 2 == 0])

    print("\nIf the value returned from the iterator isn't used in your expression you can use a _ to discard it")
    print([randint(0, 100) for _ in range(10)])


if __name__ == "__main__":
    run_demo()
