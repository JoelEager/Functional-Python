"""
Iterator creation, composition, and mapping using Python built-ins and the itertools module.

Docs:
    https://docs.python.org/3/howto/functional.html#built-in-functions
    https://docs.python.org/3/howto/functional.html#the-itertools-module
    https://docs.python.org/3/library/itertools.html
"""

from math import sqrt
from itertools import chain, accumulate, permutations, combinations, product


def skip_odd_numbers(value):
    """
    Example filter function
    """
    return value % 2 == 0


def square_it(value):
    return value ** 2


def run_demo():
    print("Nothing special about this, just a standard counting loop")
    for index in range(10):
        print(index)

    print("\nBut using iterator composition we can filter that")
    for index in filter(skip_odd_numbers, range(10)):
        print(index)

    print("\nUsing a lambda can make that more concise")
    for index in filter(lambda value: value % 2 == 0, range(10)):
        print(index)

    print("\nAdding a map() call allows us to also changes the values")
    for index in map(square_it, filter(lambda value: value % 2 == 0, range(10))):
        print(index)

    print("\nIterators can be consumed by the list constructor to produce a list")
    values = list(map(square_it, filter(lambda value: value % 2 == 0, range(10))))
    print(values)

    print("\nsum() is another built-in that consumes iterators")
    print(sum(map(square_it, filter(lambda value: value % 2 == 0, range(10)))))

    print("\nNote that each of these calls only produces another iterator.\n"
          "To actually run them you need to consume the iterator.")
    iter_out = map(sqrt, values)
    print(iter_out)
    print(list(iter_out))

    print("\nOutput from multiple iterators can be \"merged\" using itertools.chain()")
    odd_iter = filter(lambda value: value % 2 == 0, range(10))
    even_iter = filter(lambda value: value % 2 == 1, range(10))
    both_iter = chain(odd_iter, even_iter)
    print(list(both_iter))

    print("\nItertools can also help when combining elements")
    print("Accumulation:", list(accumulate(range(5))))
    print("Combinations:", list(combinations(range(3), 2)))
    print("Permutations:", list(permutations(range(3), 2)))
    print("Permutations with repetition:", list(product(range(3), repeat=2)))


if __name__ == "__main__":
    run_demo()
