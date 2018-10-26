"""
Function composition using Python decorators and nested functions.

Docs:
    https://docs.python.org/3/library/functools.html#functools.wraps
"""

from functools import wraps, lru_cache
from datetime import datetime


def log_time(func):
    """
    Decorator for logging the execution time of a function
    """
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        # The asterisks allow for any number of args and kwargs
        start = datetime.now()

        result = func(*args, **kwargs)

        seconds = (datetime.now() - start).total_seconds()
        print("{}() returned after {} seconds".format(func.__name__, seconds))

        return result

    return wrapped_function


def naive_fib(iterations):
    """
    Example of a function that can have a long run time
    """
    if 0 <= iterations <= 1:
        return iterations
    else:
        return naive_fib(iterations - 1) + naive_fib(iterations - 2)


@log_time
def timed_fib(iterations):
    """
    naive_fib() but with the log_time decorator
    """
    return naive_fib(iterations)


@log_time
@lru_cache(maxsize=128)
def cached_fib(iterations):
    """
    naive_fib() but with both caching and log_time decorators
    """
    return naive_fib(iterations)


def run_demo():
    # See how the log_time decorator can wrap arbitrary functions to produce a new composite function
    print("fib(30) ->", timed_fib(30), "\n")

    # Multiple decorators can be used to combine multiple behaviors
    print("fib(30) ->", cached_fib(30), "\n")

    print("But now thanks to the cache...")
    print("fib(30) ->", cached_fib(30))


if __name__ == "__main__":
    run_demo()
