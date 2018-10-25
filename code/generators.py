"""
Iterator creation using Python generator syntax.

Docs:
    https://docs.python.org/3/howto/functional.html#generators
    https://docs.python.org/3/tutorial/classes.html#generator-expressions
"""

from random import randint


def random_gen(max_int=100, min_int=0, num_entries=None):
    """
    A generator-based take on the RandomIter class from the custom iterators example
    """
    while num_entries != 0:
        if num_entries is not None:
            num_entries -= 1

        yield randint(min_int, max_int)     # Execution resumes here when next() is called again

    # The Python interpreter will automatically raise StopIteration when the function exits


def run_demo():
    print("Generators are another way to create custom iterators")
    print(list(random_gen(num_entries=10)))

    print("\nOften times they're far more concise than the class-based approach")

    print("\nAdditionally, generators can be created using comprehension syntax")
    rand_comp = (randint(0, 100) for _ in range(10))
    print(list(rand_comp))


if __name__ == "__main__":
    run_demo()
