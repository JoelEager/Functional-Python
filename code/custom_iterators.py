"""
Manually creating iterators using a class that implements the __iter__() and __next__() functions.

Docs:
    https://docs.python.org/3/tutorial/classes.html#iterators
"""

from random import randint


class RandomIter:
    """
    Example custom iterator
    """

    def __init__(self, max_int=100, min_int=0, num_entries=None):
        self.max_int = max_int
        self.min_int = min_int
        self.num_entries = num_entries

    def __iter__(self):
        """
        Called by the Python interpreter to create or start the iterator
        """
        return self

    def __next__(self):
        """
        Returns the next value in the iterator or raises StopIteration if it's out of entries
        """
        if self.num_entries is not None:
            if self.num_entries == 0:
                raise StopIteration
            else:
                self.num_entries -= 1

        return randint(self.min_int, self.max_int)


def run_demo():
    print("Custom iterators are convenient for producing a custom source of data")
    print(list(iter(RandomIter(num_entries=10))))

    # Custom iterators also work really well for consuming paginated API endpoints


if __name__ == "__main__":
    run_demo()
