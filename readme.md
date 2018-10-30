# Functional Python
*An introduction to solving the world’s problems with iterators.*

This repo contains the slides and code examples for my seminar on functional programming in Python. The intention is 
that you can follow along in the examples during the talk and then reference them in the future when you try writing 
functional Python code of your own. However, this can also be used as a self-guided introduction by reading through the 
slides and examples.

## Setup
All you need for these examples is **Python 3.3** or newer. Just clone the repo and run any of the examples.

## Contents
Below is a breakdown of what this repo contains. The files are listed in the recommended order for reading through the 
content:
* `slides.pdf` - Provides a general introduction to what functional programming is and how it relates to Python.
* `code/functions.py` - Shows how functions in Python are also objects and what that allows you to do.
* `code/decorators.py` - Demos function composition using Python decorators and nested functions.
* `code/iterators.py` - Makes use of python built-ins and the `itertools` modules to show how to process data through 
iterators.
* `code/comprehensions.py` - Shows an alternate use of iterators to populate Python data structures in a compact and 
readable way.
* `code/custom_iterators.py` - Demos how to create a custom iterator using a Python class.
* `code/generators.py` - Illustrates one of the lesser known Python features that allows you to turn functions into 
iterators.

## Further reading
Much of the content and structure of this seminar is based on the 
[official Python functional programming how-to](https://docs.python.org/3/howto/functional.html).
It's a great resource so if you're looking for more check it out.
