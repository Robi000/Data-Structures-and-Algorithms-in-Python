
# * -------------------------------------------------
# * -------------------------------------------------
# * -------------------------------------------------
# ! Iterators
"""
By these definitions,
an instance of a list
is an iterable, but
not itself an iterator.
"""

x = [1, 2, 3, 4]

# list is not itrator
# next(x) will not work

x = iter(x)
next(x)  # return 1
next(x)  # return 2
next(x)  # return 3
next(x)  # return 4

"""
Iterables are objects that can be iterated in iterations.

Objects like lists, tuples, sets, dictionaries, strings,
etc. are called iterables. In short and simpler terms,
iterable is anything that you can loop over.

Iterable has an in-built dunder method __iter__.

dir(X) will give us
... '__init__', '__init_subclass__', '__iter__', '__le__', '__length_ ...
look at the _iter_

Iterator supports in-built dunder methods such as  __iter__ and __next__

Iterators can only move forward using __next__. 
But remember that, iterators cannot go back or cannot be reset.

"""
# Use iterables in for-loops for multiple times
number_iterable = [1, 2, 3]
for i in number_iterable:
    print(i)
print('-----')
for i in number_iterable:
    print(i)
print('-----')
# Use iterators in for-loops for multiple times
number_iterator = iter([1, 2, 3])
for i in number_iterator:
    print(i)
print('-----')
for i in number_iterator:
    print(i)
# nothing is printed because there is no back or can not be reset...

"""
the iterator can be used just once, as completing the first for loop
has already made the iterator iterate all elements such that no more elements to be iterated.

Iterables
    Can be iterated using for loop.
    Iterables support iter() function.
    Iterables are not Iterators.
Iterators
    Can be iterated using for loop.
    Iterators suppports iter() and next() function.
    Iterators are also Iterables.
"""

# * -------------------------------------------------
# * -------------------------------------------------
# * -------------------------------------------------

# ! generator

"""
In Python, a generator is a function that returns an iterator 
that produces a sequence of values when iterated over.

Generators are useful when we want to produce a large sequence 
of values, but we don't want to store all of them in memory at
once
"""


def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1


# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)


# example 2
# efficient way of accruing factors of

def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k  # ----> k * n // k = k
            yield n // k  # so we are yilding one at a time
        k += 1
    if k * k == n:
        yield k

# * -------------------------------------------------
# * -------------------------------------------------
# * -------------------------------------------------

# ! Packing of Sequences

# automatic packing


"""
If a series of comma-separated expressions are given in 
a larger context, they will be treated as a single tuple
, even if no enclosing parentheses are provided.
"""

data = 2, 4, 6, 8  # automatic packing
# -> data = (2, 4, 6, 8)
x, y, z = (1, 2, 3)
# x = 1
# y = 2
# z = 3

# * -------------------------------------------------
# * -------------------------------------------------
# * -------------------------------------------------

# ! Scopes and Namespaces

"""
A namespace is a system that has a unique name for each and 
every object in Python. An object might be a variable or a 
method. Python itself maintains a namespace in the form of a 
Python dictionary.
"""
