# modules are abstractions that allow us to organize functions, classes and other data together in a structured way
# python comes with several built-in modules to make our lives easier
# an example of a built-in module is the random module. to use it, one must first import it by using the import keyword

import random

# the random module generate random number and random choices

# this prints a random number between 1 and 10
print(random.randint(1,10))

import datetime

now = datetime.datetime.now()
# this prints the current datetime
print(now)

# this prints the current year
print(now.year)

# this adds 28 days to our original datetime object
print(now + datetime.timedelta(days=28))
