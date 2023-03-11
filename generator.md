# Term

iterables : 
    sequence types (lists,tuples,strings) and some container objects ( dictionaries, sets,and file object) 
    are like staircases. You can visit each element one by one. Iterables contain a countable number of values
    thar are stored in memory

iterator  :  
    An iterator is an object thar implements the iterator protocol , which consists of the methods __iter__()
    and __next__()
    When you use a for loop to interate over an iterable like a list, the iterable object is passed to the
    built-in inter() funtion, which returns an iterator object.Although the iterable object contains the items,
    the iterator object keeps track of which item is  next to be used in a loop.

generator functions:
    Generator functions are a special kind of function thar return a lazy iterator called a generator iterator.
    These are object that you can loop over like a list. However, unlike a lists, lazy iterators do not store 
    their contents in memory.
    A generator iterator generates and returns a value on each call of its __next__() mothod.When the object runs out of
    values to return it. it raises a stopIteration exception.

The yield keyword
    The "yeild" keyword control the flow of generator function. This is similar to a return statement used for returning 
    values  in python.However, there is difference.

    When you call a function thar has a yeild statement,as soon as a yeild is encountered, the execution of the function
    halfs and returns a generator iterator object instead of simply returning a value. The state of the function, which
    includes variables bindings, the instruction pointer, the internal stack, and a few other things, is saved.

    In order words, the "yeild" keyword will convert an expression that is specified along with it to a generator iterator.
    and return it to the caller.

    If you want to get the value inside the generator object, you need to iterate over it. you can iterate over it using 
    for loops or special function like next().

Example : generator.py






