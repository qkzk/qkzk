#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:module: ap2_decorators  
:author: FIL - Faculté des Sciences et Technologies -  Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: 2018, september

"""

from functools import wraps


def trace(fct):
    '''
    Decorator for tracing every call to fct.
    Recursive calls are indented.

    :Example:

    >>> @trace
    ... def fact(n):
    ...     if n == 0:
    ...         return 1
    ...     else:
    ...         return n * fact(n - 1)
    
    >>> fact(5)
     -> fact((5,), {})
    ... -> fact((4,), {})
    ...... -> fact((3,), {})
    ......... -> fact((2,), {})
    ............ -> fact((1,), {})
    ............... -> fact((0,), {})
    ............... <- 1
    ............ <- 1
    ......... <- 2
    ...... <- 6
    ... <- 24
    <- 120
    120
    '''
    @wraps(fct)
    def wrapper(*args, **kwargs):
        dots = '...' * wrapper.__depth
#        print('{:s} -> {:s}{:s}'.format(dots, wrapper.__name__, repr((args, kwargs))))
        print('{:s} -> {:s}{:s}'.format(dots, wrapper.__name__, repr(args)))
        wrapper.__depth += 1
        y = fct(*args, **kwargs)
        wrapper.__depth -= 1
        print('{:s} <- {:s}'.format(dots, repr(y)))
        return y
    wrapper.__depth = 0
    return wrapper

def count(fct):
    '''
    decorator for counting  calls to  function fct
    
    :Example:

    >>> @count
    ... def fact(n):
    ...     if n == 0:
    ...         return 1
    ...     else:
    ...         return n * fact(n - 1)
    
    >>> fact.counter
    0
    >>> fact(5)
    120
    >>> fact.counter
    6
    '''
    @wraps(fct) 
    def wrapper(*args, **kwargs):
        y = fct(*args, **kwargs)
        wrapper.counter += 1
        return y
    wrapper.counter = 0
    return wrapper


def memoize(fct):
    '''
    decorator for memoizing computed values of  function fct
    
    :Example:

    >>> @count
    ... @memoize
    ... def fact(n):
    ...     if n == 0:
    ...         return 1
    ...     else:
    ...         return n * fact(n - 1)
    
    >>> fact.counter
    0
    >>> fact(5)
    120
    >>> fact.counter
    6
    >>> fact.counter = 0
    >>> fact(5)
    120
    >>> fact.counter
    1
    '''
    cache = dict()
    @wraps(fct)
    def wrapper(*args, **kwargs):
        key = repr((args, kwargs))
        if key in cache:
            return cache[key]
        else:
            y = fct(*args, **kwargs)
            cache[key] = y
            return y
    return wrapper



if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    
    







